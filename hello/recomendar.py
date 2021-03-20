# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
#from selenium import webdriver
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
    
    for curso in soup_page.findAll('script'):
        print(curso.string)
        #script_text = curso.find('results')
        #print(script_text)
        data = json.loads(curso.string)
        
    script_text = soup_page.find('script').string
    #print(script_text)
    relevant = script_text[script_text.index('=')+1:] #removes = and the part before it
    #data = json.loads(relevant) #a dictionary!
    #print(json.dumps(data, indent=4))
    
    script = soup_page.findAll('script')[1].string
    data = script.split("bootstrapData['menuMonthWeeks'] = ", 1)[-1].rsplit(';', 1)[0]
    #data = json.loads(data)
    print(data)
    
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
        print(dict)
    return listado_cursos
    
#get_info_coursera('ingles')

'''========================================================================='''
'''Obtención en Udemy'''
'''========================================================================='''

#def get_udemy(filtro):    
#    for i in range(1,cant_pag):
#        #https://www.udemy.com/courses/search/?p=2&q=machine+learning&src=ukw
#        driver = webdriver.Chrome(executable_path='D:\maria\instaladores\chromedriver_win32\chromedriver.exe')
#        url = "https://www.udemy.com/courses/search/?p="+ str(i)+"&q="+filtro+"&src=ukw"
#        print(url)
#        listado_cursos = []
#        driver.get(url)
#        sleep(5)
#        soup = BeautifulSoup(driver.page_source, "lxml")
#
#        for course in soup.select('div.course-list--container--3zXPS > div.popper--popper--19faV.popper--popper-hover--4YJ5J'):
#            dict={}
#            name = course.select_one('div.udlite-focus-visible-target.udlite-heading-md.course-card--course-title--2f7tE').get_text(strip=True)
#            #price = course.select_one('div.price-text--price-part--Tu6MH.course-card--discount-price--3TaBk.udlite-heading-md span > span').get_text(strip=True).replace('\xa0€','')
#            organizacion = course.select_one('div.udlite-text-xs.course-card--instructor-list--lIA4f').get_text(strip=True)
#            rating = course.select_one('span.udlite-sr-only').get_text(strip=True)
#            dificultad = course.select_one('div.udlite-text-xs.course-card--row--1OMjg.course-card--course-meta-info--1hHb3').get_text(strip=True)
#            
#            dict['Titulo'] = name
#            dict['Organizacion'] = organizacion
#            #dict['Precio'] = price
#            dict['Rating'] = rating
#            dict['Dificultad'] = dificultad
#            listado_cursos.append(dict)
#        driver.close()   
#    return listado_cursos
#      
#get_udemy('machine+learning')    

