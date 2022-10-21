from django.shortcuts import render
from .forms import Valueform
from .clasificacion import clasifica


def index(request):
    form = Valueform(initial={'busqueda': '',})
    return render(request, "index.html", {'form': form})
    
    if request.method == 'POST':
        form = Valueform(request.POST)
        if form.is_valid():
            parametro = form.cleaned_data['req']
            #3prediccion = clasifica(parametro)
            prediccion = 'edificio'
        return render(request, "index.html", {'form': form,'prediccion': prediccion})
    else:
        form = Valueform(initial={'busqueda': '',})
    return render(request, "index.html", {'form': form})
    
