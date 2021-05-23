# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import os
from selenium import webdriver

#from time import sleep

cant_pag = 5

'''========================================================================='''
'''Obtención en Coursera'''
'''========================================================================='''

def get_info_coursera(filtro):
  filtro = 'search?query='+filtro
  listado_cursos = []
  for i in range(1,cant_pag):
      #https://www.coursera.org/search?query=ingles&page=1&index=prod_all_products_term_optimization
    url = "https://www.coursera.org/"+filtro+"&page="+str(i) + "&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup_page = BeautifulSoup(page.content, 'html.parser')
    
    #for curso in soup_page.findAll('script'):
        #print(curso.string)
        #script_text = curso.find('results')
        #print(script_text)
        #data = json.loads(curso.string)
        
    #script_text = soup_page.find('script').string
    #print(script_text)
    #relevant = script_text[script_text.index('=')+1:] #removes = and the part before it
    #data = json.loads(relevant) #a dictionary!
    #print(json.dumps(data, indent=4))
    
    #script = soup_page.findAll('script')[1].string
    #data = script.split("bootstrapData['menuMonthWeeks'] = ", 1)[-1].rsplit(';', 1)[0]
    #data = json.loads(data)
    #print(data)
    
    for curso in soup_page.findAll("li", { "class" : "ais-InfiniteHits-item" }):
        dict={}
        print(curso)
        dict['Titulo'] = curso.find('h2').get_text()
        #dict['Link'] = curso.find('a').get_text()
        dict['Organizacion'] = curso.find('span', class_ = 'partner-name m-b-1s').get_text()
        dict['Tipo'] = curso.find('div', class_ = '_jen3vs _1d8rgfy3').get_text()
        if curso.find('span', class_ = 'ratings-text') is not None:
            dict['Rating'] = curso.find('span', class_ = 'ratings-text').get_text()
        if curso.find('span', class_ = 'difficulty') is not None:
            dict['Dificultad'] = curso.find('span', class_ = 'difficulty').get_text()
        if curso.find('span', class_ = 'enrollment-number') is not None:
            dict['Alumnos Matriculados'] = curso.find('span', class_ = 'enrollment-number').get_text()
        listado_cursos.append(dict)
        #print(dict)
    return listado_cursos
    
#get_info_coursera('ingles')

'''========================================================================='''
'''Obtención en Formate.pe'''
'''========================================================================='''

def get_info_formate(filtro):
    url = "https://www.formate.pe/resultados-busqueda.php?q="+filtro
    page = requests.get(url)
    soup_page = BeautifulSoup(page.content, 'html.parser')
    #print(soup_page)
    listado_cursos = []
  
    for curso in soup_page.findAll("article", { "class" : "item" }):
        dict={}
        dict['Titulo'] = curso.find('h4').get_text()
        dict['Descripcion'] = curso.find("p", { "class" : "descripcion" }).get_text() 
        dict['Link'] = 'https://www.formate.pe/' + curso.find('a')['href']
        listado_cursos.append(dict)
        #print(dict)
    return listado_cursos
    
#get_info_formate('ingles')

'''========================================================================='''
'''Obtención en Crehana'''
'''========================================================================='''

def get_info_crehana(filtro):
    url = "https://www.crehana.com/pe/cursos-online/search/?q="+filtro
    page = requests.get(url)
    #soup_page = BeautifulSoup(page.content, 'html.parser')
    #soup_page = BeautifulSoup(page.content, 'html5lib')
    soup_page = BeautifulSoup(page.content, 'lxml')
    #print(soup_page.text)
    #print(soup_page.select_one('.field-label:contains("Price:") + div .field-item').text)
    #print(soup_page.select_one('.html:contains("marketing")').text)
    listado_cursos = []
    #prueba = soup_page.xpath('//a[contains(@href, "image")]')
    #print(prueba)#script_text = soup_page.find(' ')
    #print(script_text)
    i=0
    for tag in soup_page.find('html').find_all():
        i=i+1
        texto = tag.get_text()
        result = texto.find(filtro)
        #print(i,result)
        if (result != -1 and i>=60 and i<68):
            relevant = texto[texto.index('{'):] #removes = and the part before it
            relevant = relevant[:relevant.index('window.__PAGE_DATA__')-19] #removes = and the part before it
            #print(relevant)
            data = json.loads(relevant) #a dictionary!
            #print(data.keys())
            for keys in data:
                texto2 = data[keys]
                #.get_text().find(filtro)
                print('validar', texto2)
                #busqueda = texto2.find(filtro)
                #if (busqueda != -1):
                #    print('validar', texto2)
        #if i>=105 and i<145:
        #    print(tag.extract())

    #for curso in soup_page.findAll('script'):
     #   print(curso.string)
    
    #for curso in soup_page.findAll('div'):
      #  print(curso.get_text())
    
    #for curso in soup_page.findAll("div", { "class" : "sc-1dd6qyt-0 hoLLHg p-4 sm:p-8 md:p-12" }):
    for curso in soup_page.findAll("div", { "class" : "sc-1dd6qyt-0 hoLLHg p-4 sm:p-8 md:p-12" }):
        print(curso)
        dict={}
        dict['Titulo'] = curso.find('div').get_text()
        listado_cursos.append(dict)
        print(dict)
    return listado_cursos
    
#get_info_crehana('marketing')
    
        
'''========================================================================='''
'''Obtención en Udemy'''
'''========================================================================='''
#https://romik-kelesh.medium.com/how-to-deploy-a-python-web-scraper-with-selenium-on-heroku-1459cb3ac76c

def get_udemy(filtro):    
    for i in range(1,cant_pag):
        #https://www.udemy.com/courses/search/?p=2&q=machine+learning&src=ukw
        driver = webdriver.Chrome(executable_path='D:\maria\instaladores\chromedriver_win32\chromedriver.exe')
                
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--disable-dev-shm-usage")
        #chrome_options.add_argument("--no-sandbox")        
        #chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        
        url = "https://www.udemy.com/courses/search/?p="+ str(i)+"&q="+filtro+"&src=ukw"
        #print(url)
        listado_cursos = []
        driver.get(url)
        #sleep(5)
        soup = BeautifulSoup(driver.page_source, "lxml")

        for course in soup.select('div.course-list--container--3zXPS > div.popper--popper--19faV.popper--popper-hover--4YJ5J'):
            dict={}
            name = course.select_one('div.udlite-focus-visible-target.udlite-heading-md.course-card--course-title--2f7tE').get_text(strip=True)
            #price = course.select_one('div.price-text--price-part--Tu6MH.course-card--discount-price--3TaBk.udlite-heading-md span > span').get_text(strip=True).replace('\xa0€','')
            organizacion = course.select_one('div.udlite-text-xs.course-card--instructor-list--lIA4f').get_text(strip=True)
            rating = course.select_one('span.udlite-sr-only').get_text(strip=True)
            dificultad = course.select_one('div.udlite-text-xs.course-card--row--1OMjg.course-card--course-meta-info--1hHb3').get_text(strip=True)
            
            dict['Titulo'] = name
            dict['Organizacion'] = organizacion
            #dict['Precio'] = price
            dict['Rating'] = rating
            dict['Dificultad'] = dificultad
            listado_cursos.append(dict)
        driver.close()   
    return listado_cursos
      
#get_udemy('marketing')    

