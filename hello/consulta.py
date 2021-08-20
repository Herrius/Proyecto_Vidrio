# -*- coding: utf-8 -*-

from newspaper import Config
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
import nltk
import io
import base64
import tweepy 
from sentiment_analysis_spanish import sentiment_analysis
import re

#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
#config = Config()
#config.browser_user_agent = user_agent
#
stopwords = nltk.corpus.stopwords.words('spanish')
stopwords.append('----')
stopwords.append('---')
stopwords.append('--')
stopwords.append(':')
stopwords.append(',')
stopwords.append('!')
stopwords.append('/')
stopwords.append('.')
stopwords.append('?')
stopwords.append('"')
stopwords.append('>')
stopwords.append('htpps')
stopwords.append('co')
stopwords.extend(['…','(',')','“','”',"''",'``','•',';'])

def get_noticias(keywords):
    lista=[]
    lista = get_news_google3(keywords)
    return lista   

def generate_wordcloud(text): 
    wordcloud = WordCloud(
         background_color="white", max_words=5000, 
         min_font_size = 10, 
         max_font_size=100, 
         #relative_scaling = 0.5, 
         stopwords=stopwords,
         scale=3,
         random_state=3)
         #normalize_plurals= True)
    wordcloud.generate(text)
    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    sio = io.BytesIO()
    plt.savefig(sio, format='png')
    encoded_img = base64.b64encode(sio.getvalue())    
    image_64 = 'data:image/png;base64,' + urllib.parse.quote(encoded_img)
    #image_64 = '<img src="data:image/png;base64,' + urllib.parse.quote(encoded_img) + '" />'
    sio.close()
    return image_64

def get_estadisticas(lista):  
    lista_tokens=[]
    for i in lista:    
        mensaje = i["Titulo"]
        words = nltk.word_tokenize(mensaje)
        lista_tokens.extend(words)
        
    lista_tokens_final = [term for term in lista_tokens if term not in stopwords]
        
#    print('Distribución de Frequencia de Todas las Palabras')
#    fdist_todos = nltk.FreqDist(lista_tokens_final)
#    print('50 palabras mas frequentes',fdist_todos.most_common(50))
#    fdist_todos.plot(30, cumulative=False)    
        
    terms_only_string = " ".join(str(v) for v in lista_tokens_final)
    imagen = generate_wordcloud(terms_only_string)
    return imagen

#obtener noticias usando el url https://news.google.com/rss/
def get_news_google3(filtro):
    lista=[]
    limite=5
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    rango_tiempo = '+when:30d'
    url_new = 'https://news.google.com/rss/search?q=' + filtro + rango_tiempo + '&sort=date&hl=es-419&gl=PE&ceid=PE:es-419'
    rss_text = urllib.request.urlopen(url_new).read().decode('utf8')
    soup_page=BeautifulSoup(rss_text,"xml")
    i=0
    for news in soup_page.findAll("item"):
        i=i+1
        dict={}
        fecha_str = datetime.strptime(news.pubDate.text, '%a, %d %b %Y %H:%M:%S GMT')
        dict['Fecha']=fecha_str
        dict['Titulo']=news.title.text
        #dict['Mensaje']=news.description.text
        dict['Origen']=news.source.text
        dict['Link']=news.link.text
        lista.append(dict)
        if i > limite:
            break;
    return lista

#######################################################################################
#######################################################################################
#Credenciales del Twitter API
access_key = "1245052506687840256-hHElUU88rTqvbRv0bgKhRUezca1FZB"
access_secret = "CeJk6qu3qWRzNQcYzp7b2iWbzX2riPXWn2c4j8BLZoyOo"
consumer_key = "a8yUX9SrhHa0bvyl53HEgF80G"
consumer_secret = "Y7uYgbkIcdBA6YopQlqnZfNuo3LKvKklKPIJuCUnXafA2SLPmZ"

'''Método de Autenticación para conectarse a twitter'''
def autenticacion():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api

def get_estadisticasTwitter(lista_tokens_final):  
      
#    print('Distribución de Frequencia de Todas las Palabras')
#    fdist_todos = nltk.FreqDist(lista_tokens_final)
#    print('50 palabras mas frequentes',fdist_todos.most_common(50))
#    fdist_todos.plot(30, cumulative=False)    
        
    terms_only_string = " ".join(str(v) for v in lista_tokens_final)
    imagen = generate_wordcloud(terms_only_string)
    return imagen

def preprocess(s):
    emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
        
    regex_str =[emoticons_str,
                r'<[^>]+>' , #HTML tags
                r'(?:@[\w_]+)' , #@-Mención
                r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)" , #Hash-tags
                r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', #URLs
                r'(?:[\w_]+)' , #Otras Palabras
                r'(?:\S)' #Otras Palabras
                ]    
    
    tokens_re = re.compile (r'('+'|'.join(regex_str)+')' ,re.VERBOSE | re.IGNORECASE)
    tokens = tokens_re.findall(s)
    return tokens

def GraficarDatos(numeros_list,popularidad_list,numero,nombre):
    axes = plt.gca()
    axes.set_ylim([-1, 2])
    
    plt.scatter(numeros_list, popularidad_list)
    popularidadPromedio = (sum(popularidad_list))/(len(popularidad_list))
    popularidadPromedio = "{0:.0f}%".format(popularidadPromedio * 100)
    #print(popularidadPromedio)
    #time1  = datetime.now().strftime("A : %H:%M\n El: %m-%d-%y")
    '''plt.text(0, 1.25, 
             "Sentimiento promedio:  " + str(popularidadPromedio) + "\n", 
             fontsize=12, 
             bbox = dict(facecolor='none', 
                         edgecolor='black', 
                         boxstyle='square, pad = 1'))
    '''
    plt.title("Sentimientos en twitter")
    plt.xlabel("Numero de tweets")
    plt.ylabel("Sentimiento")
    sio = io.BytesIO()
    plt.savefig(sio, format='png')
    encoded_img = base64.b64encode(sio.getvalue())    
    image_64 = 'data:image/png;base64,' + urllib.parse.quote(encoded_img)
    #image_64 = '<img src="data:image/png;base64,' + urllib.parse.quote(encoded_img) + '" />'
    sio.close()
    return image_64
    
def tweets_x_filtro(screen_name):
    search_words = screen_name
    date_since = "2021-08-15"
    new_search = search_words + " -filter:retweets"
    count=0
    limite=5
    api = autenticacion()
    popularidad_list = []
    numeros_list = []
    tweets_tokens_all=[]
    
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    for tweet in tweepy.Cursor(api.search,
              q=new_search,
              lang="es",
              since=date_since).items(limite):        
        count= count + 1   
        full_text = tweet.text
        newTexto = sentiment.sentiment(full_text)
        popularidad_list.append(newTexto)
        numeros_list.append(count)
        
        "#Crea una lista con todos los términos sin stop"
        terms_all = [term for term in preprocess(full_text) 
                            if term not in stopwords]
                
        tweets_tokens_all.extend(terms_all)
        
    print(count)     
    imagenT = GraficarDatos(numeros_list,popularidad_list,count,'')
    imagenT2 = get_estadisticasTwitter(tweets_tokens_all)
    return imagenT, imagenT2
    #print("total de tweets", count)
    
#tweets_x_filtro('coronavirus')

#get_news_google3('covid')
#lista = get_noticias(['gamarra'])    
#print(lista)
#estadisticas = get_estadisticas(lista)
