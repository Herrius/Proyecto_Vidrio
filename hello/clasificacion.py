# -*- coding: utf-8 -*-

from pickle import load
from sklearn import svm
        
def cargar_modelo(nombre): 
    input = open(nombre,  'rb')
    modelo = load(input)
    input.close()   
    return modelo

def clasifica(datos):    
    listado = datos.split(sep=',')
    listado2 = [listado]
    ruta = 'hello/modelos/'
    nombre='modelo2.pkl'
    modelo = cargar_modelo(ruta+nombre)
    print(listado)
    tipo = modelo.predict(listado2)
    return tipo

def predict_titanic(input_features):
    ruta = 'hello/modelos/'
    nombre = 'titanic.pkl'  # Asegúrate de cambiar esto por el nombre de tu modelo de cáncer
    modelo = cargar_modelo(ruta + nombre)
    print([input_features])
    prediction = modelo.predict([input_features])
    print(prediction[0])
    return prediction[0]