from django.shortcuts import render
from django.http import HttpResponse
from .forms import Valueform
from .models import Greeting
import recomendar

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
            parametro = form.busqueda
            listado = recomendar.get_info_coursera(parametro)
    return render(request, "index2.html", {'listado': listado})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
