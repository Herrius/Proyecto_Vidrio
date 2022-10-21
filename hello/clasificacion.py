# -*- coding: utf-8 -*-

from pickle import load

        
def cargar_modelo(nombre): 
    input = open(nombre,  'rb')
    modelo = load(input)
    input.close()   
    return modelo

def clasifica(datos):
    
    listado = datos.split(sep=';')
    nombre='modelo.pkl'
    modelo = cargar_modelo(nombre)
    tipo = modelo.predict(datos)
    return tipo
