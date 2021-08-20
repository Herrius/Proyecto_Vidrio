from django.shortcuts import render
from django.http import HttpResponse
from .forms import Valueform
from .models import Greeting
from .recomendar import get_info_coursera
from .recomendar import get_udemy
from .recomendar import get_info_formate
from .recomendar import get_info_crehana
from .chatbot2 import response
from .chatbot import responseNLTK
from .dboperations import insert_db
from .consulta import get_noticias
from .consulta import get_estadisticas
from .chatbotCovid import busquedacama
from .chatbotCovid import busquedaoxigeno
from .chatbotCovid import infoVacunas
from .chatbotCovid import validaFakeNew
from .chatbotCovid import noticiasCovid
from nltk import word_tokenize

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    form = Valueform(initial={'busqueda': '',})
    return render(request, "index.html", {'form': form})

def index2(request):
    # return HttpResponse('Hello from Python!')
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Check if the form is valid:
        form = Valueform(request.POST)
        if form.is_valid():
            parametro = form.cleaned_data['busqueda']
            #listado = get_info_coursera(parametro)
            listado = get_udemy(parametro)
            listado2 = get_info_formate(parametro)
            listado3 = get_info_crehana(parametro)
    return render(request, "index2.html", {'form': form,'listado': listado,'listado2': listado2,'listado3': listado3})

def home(request):
    # return HttpResponse('Hello from Python!')
    form = Valueform(initial={'busqueda': '',})
    return render(request, "info/home.html", {'form': form})

def home2(request):
    # return HttpResponse('Hello from Python!')
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Check if the form is valid:
        form = Valueform(request.POST)
        if form.is_valid():
            parametro = form.cleaned_data['busqueda']
            #listado = get_info_coursera(parametro)
            listado = get_udemy(parametro)
            listado2 = get_info_formate(parametro)
            listado3 = get_info_crehana(parametro)
            insert_db(listado,listado2,listado3,parametro)
    return render(request, "info/home2.html", {'form': form,'listado': listado,'listado2': listado2,'listado3': listado3})

def chatbot(request):
    respon = "EDUCHATBOT: Hola, mi nombre es Robo. Contestaré todas tus preguntas, para terminar escribe Bye!"
    return render(request, "Chatbot.html", {'respon':respon})

def chatbotRespuesta(request):
    respon = ' '
#    if request.method == 'POST':
#        #respon = response(request.form['question'])
#        #print('PRUEBA'+request.POST)
#        respon = response(request.POST['question'])
#    else:
#        respon = "EDUCHATBOT: Hola, mi nombre es Robo. Contestaré todas tus preguntas, para terminar escribe Bye!"
#    return render(request, "Chatbot.html", {'respon':respon})
    respon = responseNLTK(request.GET['msg'])
    return HttpResponse(respon)

def chatbot2(request):
    respon = "EDUCHATBOT: Hola, mi nombre es Robo. Contestaré todas tus preguntas, para terminar escribe Bye!"
    return render(request, "Chatbot2.html", {'respon':respon})
    
def chatbot2Respuesta(request):
    #respon = response(request.POST['msg'])
    respon = response(request.GET['msg'])
    return HttpResponse(respon)

def chatbotCovid(request):
    respon = " "
    return render(request, "ChatbotCovid.html", {'respon':respon})
    
#1. Camas Disponibles
#2. Oxígeno Disponible
#3. Información de Vacunas
#4. Noticias Falsas (fakenews)
#5. Últimas Noticias
#6. Registro
def chatbotCovidRespuesta(request):
    chat = request.GET['msg']
    words = word_tokenize(chat)
    tipo = int(words[0])
    print('tipo:'+words[0])
    
    if tipo is None:
        tipo = chat
    
    if tipo == 1:
        if chat is None:
            mensaje = 'Ingrese provincia y distrito'
        else:
            mensaje = busquedacama(words)
    elif tipo == 2:
        if chat is None:
            mensaje = 'Ingrese provincia y distrito'
        else:
            mensaje = busquedaoxigeno(chat)
    elif tipo == 3:
        if chat is None:
            mensaje = 'Ingrese provincia y distrito'
        else:
            mensaje = infoVacunas(chat)
    elif tipo == 4:
        if chat is None:
            mensaje = 'Ingrese noticia a validar'
        else:
            mensaje = validaFakeNew(chat)
    elif tipo == 5:
        if chat is None:
            mensaje = 'Ingrese palabras principales'
        else:
            mensaje = noticiasCovid(words)
    elif tipo == 6:
    	mensaje = 'En construcción' 
    #else:
    #	mensaje = 'Escoga una opción por favor, gracias.'
    
    #respon = response(mensaje)
    return HttpResponse(mensaje)

def consulta(request):
    # return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        # Check if the form is valid:
        form = Valueform(request.POST)
        if form.is_valid():
            parametro = form.cleaned_data['busqueda']
            listado = get_noticias(parametro)
            imagenN = get_estadisticas(listado)
        return render(request, "info/consulta.html", {'form': form,'listado': listado,'imagenN': imagenN})
    else:
        form = Valueform(initial={'busqueda': '',})
        return render(request, "info/consulta.html", {'form': form})
    
def save_db(list1,list2,list3):
    print('prueba')
    insert_db(list1,list2,list3)
    
def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
