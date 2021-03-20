from django.shortcuts import render
from django.http import HttpResponse
from .forms import Valueform
from .models import Greeting
from .recomendar import get_info_coursera

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
            listado = get_info_coursera(parametro)
            listado2 = get_info_formate(parametro)
    return render(request, "index2.html", {'form': form,'listado': listado,'listado2': listado2})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
