from django.shortcuts import render
from django.http import HttpResponse
from .forms import Valueform
from .models import Greeting
from .recomendar import get_info_coursera
from .recomendar import get_udemy
from .recomendar import get_info_formate
from .recomendar import get_info_crehana
from .chatbot2 import response
from .dboperations import insert_db

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    form = Valueform(initial={'busqueda': '',})
    return render(request, "index.html", {'form': form})

def home(request):
    # return HttpResponse('Hello from Python!')
    form = Valueform(initial={'busqueda': '',})
    return render(request, "info/home.html", {'form': form})

def chatbot(request):
    respon = "EDUCHATBOT: Hola, mi nombre es Robo. Contestaré todas tus preguntas, para terminar escribe Bye!"
    return render(request, "Chatbot.html", {'respon':respon})

def chatbotRespuesta(request):
    if request.method == 'POST':
        #respon = response(request.form['question'])
        #print('PRUEBA'+request.POST)
        print('PRUEBA'+request.POST['question'])
        respon = response(request.POST['question'])
    else:
        respon = "EDUCHATBOT: Hola, mi nombre es Robo. Contestaré todas tus preguntas, para terminar escribe Bye!"
    return render(request, "Chatbot.html", {'respon':respon})

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

def save_db(list1,list2,list3):
    print('prueba')
    insert_db(list1,list2,list3)
    
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
