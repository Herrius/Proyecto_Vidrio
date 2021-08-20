# -*- coding: utf-8 -*-

from newspaper import Config
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
##from nltk import word_tokenize
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
import nltk
import io
import base64
import tweepy 
from sentiment_analysis_spanish import sentiment_analysis
#from sentiment_analysis_spanish import sentiment_analysis
#from textblob import TextBlob
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#
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
    
    #sio = io.StringIO()
    sio = io.BytesIO()
    plt.savefig(sio, format='png')
    encoded_img = base64.b64encode(sio.getvalue())    
    #image_64 = 'data:image/png;base64,' + urllib.parse.quote(encoded_img)
    image_64 = '<img src="data:image/png;base64,' + urllib.parse.quote(encoded_img) + '" />'
    
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
    limite=10
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

def save_tweets_x_filtro(screen_name):
    search_words = screen_name
    date_since = "2021-08-15"
    new_search = search_words + " -filter:retweets"
    count=0
    api = autenticacion()
    alltweets = []   
            
    tweets = tweepy.Cursor(api.search,
              q=new_search,
              lang="es",
              since=date_since).items(100)
        
    alltweets.extend(tweets)  
    print(len(alltweets)) 
    #print(alltweets)
    
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
#    for line in alltweets:        
#            count= count + 1              
#            if not line.isspace():
#                tweet = json.loads(line)
#                full_text = tweet["text"]
#                
#                if "quoted_status" in tweet:                
#                    tweet_quoted= tweet["quoted_status"]
#                    if "extended_tweet" in tweet_quoted: 
#                        tweet_extended = tweet_quoted["extended_tweet"]
#                        if "full_text" in tweet_extended: 
#                            full_text = tweet_extended["full_text"]
#                            newTexto = sentiment.sentiment(full_text)
#                            popularidad_list.append(newTexto)
#                            numeros_list.append(count)
#             
#    print("total de tweets", count)
#    GraficarDatos(numeros_list,popularidad_list,count,arc)

#save_tweets_x_filtro('covid')

#get_news_google3('covid')

#lista = get_noticias(['gamarra'])    
#print(lista)
#estadisticas = get_estadisticas(lista)
