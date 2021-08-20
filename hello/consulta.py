# -*- coding: utf-8 -*-

#from newspaper import Article
from newspaper import Config
#from urllib import request
from bs4 import BeautifulSoup
from datetime import datetime
##from datetime import timedelta
##import locale
##from newsapi import NewsApiClient
import urllib.request
##from nltk import word_tokenize
##from bs4 import BeautifulSoup
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
import nltk
import io
import base64
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
  
#obtener noticias usando el url https://news.google.com/rss/
def get_news_google3(filtro):
    lista=[]
    limite=10
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    filtro_final = "covid%"+filtro
    rango_tiempo = '+when:5d'
    url_new = 'https://news.google.com/rss/search?q=' + filtro_final + rango_tiempo + '&sort=date&hl=es-419&gl=PE&ceid=PE:es-419'
    #print(url_new)
    rss_text = urllib.request.urlopen(url_new).read().decode('utf8')
    soup_page=BeautifulSoup(rss_text,"xml")
    i=0
    for news in soup_page.findAll("item"):
        i=i+1
        dict={}
        #print(i)
        #url = news.link.text
        fecha_str = datetime.strptime(news.pubDate.text, '%a, %d %b %Y %H:%M:%S GMT')
        dict['Fecha']=fecha_str
        dict['Titulo']=news.title.text
        dict['Mensaje']=news.description.text
        dict['Origen']=news.source.text
        lista.append(dict)
        if i > limite:
            break;
    get_estadisticas(lista)
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
    
    sio = io.StringIO()
    plt.savefig(sio, format="PNG")
    encoded_img = base64.b64encode(sio.getvalue())

    #wordcloud.to_file("static/images/wc.png")
    #print("Word Cloud Saved Successfully")
    #path="wc.png"
    #filename = Image.open("wc.png")
    #filename.show() 
            
    #plt.figure(figsize=(25,25))
    #plt.imshow(wordcloud)
    #plt.axis("off")
    #plt.show()
    
    #pyplot.savefig(sio, format="PNG")
    #encoded_img = sio.getvalue().encode('Base64') # On Python 3x, use base64.b64encode(sio.getvalue())

    return encoded_img

def get_estadisticas(lista):  
    lista_tokens=[]
    for i in lista:    
        mensaje = i["Mensaje"]
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

#lista = get_noticias(['gamarra'])    
#print(lista)
#estadisticas = get_estadisticas(lista)
