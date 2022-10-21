from django.shortcuts import render
from .forms import Valueform
from .models import Greeting
from .clasificacion import clasifica

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    form = Valueform(initial={'busqueda': '',})
    return render(request, "index.html", {'form': form})
    
    if request.method == 'POST':
        form = Valueform(request.POST)
        if form.is_valid():
            parametro = form.cleaned_data['req']
            prediccion = clasifica(parametro)
            print('clasificò2222')
        return render(request, "index.html", {'form': form,'prediccion': prediccion})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Valueform(initial={'busqueda': '',})
    return render(request, "index.html", {'form': form})
    
def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
