# -*- coding: utf-8 -*-
#https://www.tutorialfor.com/blog-251181.htm
#https://github.com/gautamkrishnar/hatter/blob/master/main.py
#https://github.com/pemagrg1/Easy-Chatbot/blob/master/bot.py

import os
from aiml import Kernel
from os import listdir
from flask import Flask, url_for
from flask import g, session, request, render_template

mybot_path="./templates/aimls"
#Switch to the working directory where the corpus is located
#os.chdir(mybot_path)
#files = listdir('./templates/aimls/')
#files = listdir('./')

abs_path = os.path.abspath("./templates/aimls")
UPLOAD_DIRECTORY = "/python-getting-started/hello/templates/aimls/"
files = listdir(abs_path)

#APP
#app = Flask(__name__)
#app.config.from_object(__name__)

def response(user_response):   
    robo_response=''  
    mybot=Kernel()
    
    for file in files:
        mybot.learn(file)
    robo_response = mybot.respond(user_response)
    return robo_response

def inicio():   
    
    flag=True  
    print("ROBO: Hola, mi nombre es Robo. Contestaré todas tus preguntas, para terminar escribe Bye!")
    while(flag==True):   
        user_response = input()   
        user_response=user_response.lower()   
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
            
#respon = ' '
#
#@app.before_request
#def before_request():
#	g.respon = "EDUCHATBOT: Hola, mi nombre es Robo. Contestaré todas tus preguntas, para terminar escribe Bye!"
#
#@app.route("/chatbot")
#def home():
#    return render_template("Chatbot.html")
#
#@app.route('/chatbot2',methods=['GET','POST'])
#def index():
#	if request.method == 'POST':
#		reply = response(request.form['question'])
#		return render_template('index.html',respon=reply)
#	return render_template('index.html',respon=g.respon)
#	
##running the app
#if __name__ == "__main__":
#	app.run(debug=True)
            
            
            
            