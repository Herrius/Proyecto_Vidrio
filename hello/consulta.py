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
#from wordcloud import WordCloud 
#import matplotlib.pyplot as plt
#import nltk
#from sentiment_analysis_spanish import sentiment_analysis
#from textblob import TextBlob
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#
#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
#config = Config()
#config.browser_user_agent = user_agent
#
#stopwords = nltk.corpus.stopwords.words('spanish')
#stopwords.append('----')
#stopwords.append('---')
#stopwords.append('--')
#stopwords.append(':')
#stopwords.append(',')
#stopwords.append('!')
#stopwords.append('/')
#stopwords.append('.')
#stopwords.append('?')
#stopwords.append('"')
#stopwords.append('>')
#stopwords.extend(['…','(',')','“','”',"''",'``','•',';'])

#obtener noticias usando el url https://news.google.com/rss/
#límite de noticias sólo 100
#no se puede hacer el rango de fechas
#def get_news_google3(filtro, fecha_desde, fecha_hasta,tipo):
#    rango_tiempo = '+when:30d'
#    url_new = 'https://news.google.com/rss/search?q=' + filtro + rango_tiempo + '&sort=date&hl=es-419&gl=PE&ceid=PE:es-419'
#    #url_new = 'https://news.google.com/rss/search?q=' + filtro + '&sort=date&hl=es-419&gl=PE&ceid=PE:es-419'
#    rss_text = request.urlopen(url_new).read().decode('utf8')
#    soup_page=BeautifulSoup(rss_text,"xml")
#    i=0
#    list=[]
#    
#    for news in soup_page.findAll("item"):
#        i=i+1
#        #print(i)
#        url = news.link.text
#        fecha_str = datetime.strptime(news.pubDate.text, '%a, %d %b %Y %H:%M:%S GMT')
#        titulo = news.title.text
#        texto = news.description.text
#        origen = news.source.text
#        #print(url)
#        ind = True
#        if tipo == 0:
#            if fecha_str > datetime.strptime(fecha_desde, '%m/%d/%Y') and fecha_str < datetime.strptime(fecha_hasta, '%m/%d/%Y'):                                
#                ind = True
#            else:
#                ind = False
#        #if fecha_str > datetime.strptime(fecha_desde, '%m/%d/%Y') and fecha_str < datetime.strptime(fecha_hasta, '%m/%d/%Y'):                                
#        if ind:                                
#            fecha = fecha_str.strftime('%Y%m%d') 
#            dict={}
#            try: 
#                article = Article(url,config=config)
#                article.download()
#                article.parse()
#                article.nlp()
#                if article.publish_date is not None:                    
#                    fecha = article.publish_date.strftime('%Y%m%d') 
#                dict['Fecha']=fecha
#                dict['Titulo']=article.title
#                dict['Mensaje']=article.text
#                dict['URL']=url
#                dict['País']=''
#                dict['Like']=''
#                dict['Tipo']='Noticia'
#                dict['Banco']=filtro
#                dict['Resumen']=article.summary
#                dict['Origen']=origen
#                list.append(dict)
#            except: 
#                print("Timeout occurred")
#                dict['Fecha']=fecha
#                dict['Titulo']=titulo
#                dict['Mensaje']=texto
#                dict['URL']=url
#                dict['País']=''
#                dict['Like']=''
#                dict['Tipo']='Noticia'
#                dict['Banco']=filtro
#                dict['Resumen']=''
#                dict['Origen']=origen
#                list.append(dict)
#    return list

def get_noticias(keywords):
    lista=[]
    lista = get_news_google3(keywords)
    return lista   
  
#obtener noticias usando el url https://news.google.com/rss/
def get_news_google3(filtro):
    lista=[]
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
        if i > 10:
            break;
    return lista

#def generate_wordcloud(text): 
#    wordcloud = WordCloud(
#         background_color="white", max_words=5000, 
#         min_font_size = 10, 
#         max_font_size=100, 
#         #relative_scaling = 0.5, 
#         stopwords=stopwords,
#         scale=3,
#         random_state=3)
#         #normalize_plurals= True)
#    wordcloud.generate(text)
#    
#    wordcloud.to_file("static/images/wc.png")
#    print("Word Cloud Saved Successfully")
#    #path="wc.png"
#    #filename = Image.open("wc.png")
#    #filename.show() 
#            
#    #plt.figure(figsize=(25,25))
#    #plt.imshow(wordcloud)
#    #plt.axis("off")
#    #plt.show()
#    
#def get_estadisticas(lista):  
#    lista_tokens=[]
#    for i in lista:    
#        mensaje = i["Mensaje"]
#        words = nltk.word_tokenize(mensaje)
#        lista_tokens.extend(words)
#        
#    lista_tokens_final = [term for term in lista_tokens if term not in stopwords]
#        
#    print('Distribución de Frequencia de Todas las Palabras')
#    fdist_todos = nltk.FreqDist(lista_tokens_final)
#    print('50 palabras mas frequentes',fdist_todos.most_common(50))
#    fdist_todos.plot(30, cumulative=False)    
#        
#    terms_only_string = " ".join(str(v) for v in lista_tokens_final)
#    generate_wordcloud(terms_only_string)
        
#lista = get_noticias(['gamarra'])    
#print(lista)
#estadisticas = get_estadisticas(lista)
