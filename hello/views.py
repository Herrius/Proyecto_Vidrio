from django.shortcuts import render
from .forms import Valueform,titanicForm
from .clasificacion import clasifica,predict_titanic

def index(request):
    if request.method == 'POST':
        form = Valueform(request.POST)
        if form.is_valid():
            parametro = form.cleaned_data['busqueda']
            prediccion = clasifica(parametro)
        return render(request, "index.html", {'form': form,'prediccion': prediccion})
    else:
        form = Valueform(initial={'busqueda': '',})
        return render(request, "index.html", {'form': form})
    
def titanic(request):
    form = titanicForm(request.POST or None)
    prediccion = None
    if request.method == 'POST' and form.is_valid():
        input_features = [form.cleaned_data.get(field.name) for field in form]
        prediccion = predict_titanic(input_features)


    return render(request, 'titanic.html', {'form': form, 'prediccion': prediccion})
