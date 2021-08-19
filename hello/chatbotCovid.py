# -*- coding: utf-8 -*-

import os
from aiml import Kernel
from os import listdir
#from newspaper import Config
import urllib.request
from bs4 import BeautifulSoup
import json
from nltk import word_tokenize

path = os.path.dirname(os.path.realpath(__file__))
#abs_path = os.path.abspath("templates/aimls") #desarrollo
abs_path = os.path.abspath("hello/templates/aimls") #produccion
files = listdir(abs_path)
mybot=Kernel()
    
for file in files:
    mybot.learn(path + '/templates/aimls/' + file)

def busquedacama(user_response):   
    robo_response=''  
    words = word_tokenize(user_response)
    robo_response = apiCamaSusalud(words[0], words[1])
    print('RESPUESTA'+robo_response)
    return robo_response

def busquedaoxigeno(user_response):   
    robo_response=''  
    robo_response = apiOxigenoSusalud('SANTA', 'CHIMBOTE')
    print('RESPUESTA'+robo_response)
    return robo_response

def infoVacunas(user_response):   
    robo_response=''  
    robo_response = mybot.respond(user_response)
    print('RESPUESTA'+robo_response)
    return robo_response

def validaFakeNew(user_response):   
    robo_response=''  
    robo_response = mybot.respond(user_response)
    print('RESPUESTA'+robo_response)
    return robo_response

def noticiasCovid(user_response):   
    robo_response=''  
    #robo_response = get_news_google3(user_response)
    print('RESPUESTA'+robo_response)
    return robo_response

#CHATBOT basado en aimls
def response(user_response):   
    robo_response=''  
    robo_response = mybot.respond(user_response)
    print('RESPUESTA'+robo_response)
    return robo_response

#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
#config = Config()
#config.browser_user_agent = user_agent
#
##obtener noticias usando el url https://news.google.com/rss/
#def get_news_google3(filtro):
#    filtro_final = "covid%"+filtro
#    #rango_tiempo = '+when:30d'
#    rango_tiempo = '+when:5d'
#    url_new = 'https://news.google.com/rss/search?q=' + filtro_final + rango_tiempo + '&sort=date&hl=es-419&gl=PE&ceid=PE:es-419'
#    print(url_new)
#    rss_text = urllib.request.urlopen(url_new).read().decode('utf8')
#    soup_page=BeautifulSoup(rss_text,"xml")
#    i=0
#    respuesta_final = ''
#    for news in soup_page.findAll("item"):
#        i=i+1
#        print(i)
#        #url = news.link.text
#        #fecha_str = datetime.strptime(news.pubDate.text, '%a, %d %b %Y %H:%M:%S GMT')
#        titulo = news.title.text
#        texto = news.description.text
#        origen = news.source.text
#        total = titulo +' ' + texto + ' ' +origen 
#        print(total)
#        respuesta_final = respuesta_final + ';' + origen
#        if i > 10:
#            break;
#    return respuesta_final

def apiCamaSusalud(provincia, distrito):
    respuesta_final = ''
    limite = '100'
    url_new = 'http://datos.susalud.gob.pe/api/action/datastore/search.json?resource_id=187105ef-d71b-44e0-a5af-4762c33cefb3&limit=' + limite 
    rss_text = urllib.request.urlopen(url_new).read().decode('utf8')
    soup = BeautifulSoup(rss_text,'html.parser')
    site_json=json.loads(soup.text)
    results = site_json['result']
    for rec in results['records']:
        total_camas = ''    
        for key in rec.keys():
            try:
                a = int(rec[key])
                if a > 0 and (key.startswith('ZC') or key.startswith('ZNC')):
                    total_camas = total_camas + ',' + key + str(a)
                    #print(key, a)
            except ValueError:
                it_is = False            
        if (rec['PROVINCIA'] == provincia) and (rec['DISTRITO'] == distrito) :
            respuesta_final = respuesta_final + ';' + rec['NOMBRE'] + total_camas
    print(respuesta_final)
    return respuesta_final

def apiOxigenoSusalud(provincia, distrito):
    respuesta_final = ''
#    limite = '10'
#    url_new = 'http://datos.susalud.gob.pe/api/action/datastore/search.json?resource_id=b1791142-8fcb-4766-9b8c-b0ee0ffc6dff&limit=' + limite 
#    rss_text = urllib.request.urlopen(url_new).read().decode('utf8')
#    soup = BeautifulSoup(rss_text,'html.parser')
#    site_json=json.loads(soup.text)
#    #print(site_json)
#    results = site_json['result']
#    for i in results['records']:
#        #print(i)
#        if i['PROVINCIA'] == 'Lima':
#            respuesta_final = respuesta_final + ';' + i['NOMBRE']
    return respuesta_final
    
apiCamaSusalud('LIMA', 'SANTIAGO DE SURCO')
#get_news_google3('vacuna')