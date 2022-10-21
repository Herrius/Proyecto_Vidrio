# -*- coding: utf-8 -*-

from pickle import load
from sklearn import svm
        
def cargar_modelo(nombre): 
    input = open(nombre,  'rb')
    modelo = load(input)
    input.close()   
    return modelo

def clasifica(datos):    
    listado = datos.split(sep=';')
    ruta = '/app/hello/modelos/'
    nombre='modelo.pkl'
    modelo = cargar_modelo(ruta+nombre)
    print(listado)
    tipo = modelo.predict(listado)
    return tipo
