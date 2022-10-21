from django import forms

class Valueform(forms.Form):
    busqueda = forms.CharField(max_length = 100)

