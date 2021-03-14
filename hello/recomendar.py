# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

cant_pag = 5

listado_cursos = []


def get_info_coursera(filtro):
  filtro = 'search?query='+filtro
  for i in range(1,cant_pag):
    url = "https://www.coursera.org/"+filtro+"&page="+str(i) + "&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup_page = BeautifulSoup(page.content, 'html.parser')
    for curso in soup_page.findAll("li", { "class" : "ais-InfiniteHits-item" }):
        dict={}
        dict['Titulo'] = curso.find('h2').get_text()
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