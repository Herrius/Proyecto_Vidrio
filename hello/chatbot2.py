# -*- coding: utf-8 -*-
#https://www.tutorialfor.com/blog-251181.htm
#https://github.com/gautamkrishnar/hatter/blob/master/main.py
#https://github.com/pemagrg1/Easy-Chatbot/blob/master/bot.py
#https://studygyaan.com/python/create-web-based-chatbot-in-python-django-flask
#https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44

import os
from aiml import Kernel
from os import listdir
#from flask import Flask, url_for
#from flask import g, session, request, render_template

#mybot_path="./templates/aimls"
#os.chdir(mybot_path)
#files = listdir('./')
#UPLOAD_DIRECTORY = "/python-getting-started/hello/templates/aimls/"

path = os.path.dirname(os.path.realpath(__file__))
#abs_path = os.path.abspath("templates/aimls") #desarrollo
abs_path = os.path.abspath("hello/templates/aimls") #produccion
files = listdir(abs_path)
mybot=Kernel()
    
for file in files:
    mybot.learn(path + '/templates/aimls/' + file)


#CHATBOT basado en aimls
def response(user_response):   
    robo_response=''  
    robo_response = mybot.respond(user_response)
    print('RESPUESTA'+robo_response)
    return robo_response

def responseDeepLearning(user_response):   
    robo_response=''  
    robo_response = mybot.respond(user_response)
    print('RESPUESTA'+robo_response)
    return robo_response

def inicio():   
    
    flag=True  
    print("ROBO: Hola, mi nombre es Robo. Contestaré todas tus preguntas, para terminar escribe Bye!")
    while(flag==True):   
        user_response = input()   
        #user_response=user_response.lower()   
        if(user_response!='bye'):   
            if(user_response=='gracias' or user_response=='muchas gracias' ):   
                flag=False   
                print("ROBO: De nada, vuelva pronto")   
            else:   
                print(response(user_response))   
        else:   
            flag=False   
            print("ROBO: Adiós!")
    
#inicio() 
            
