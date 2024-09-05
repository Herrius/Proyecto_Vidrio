from django import forms

class Valueform(forms.Form):
    busqueda = forms.CharField(max_length = 100)

class titanicForm(forms.Form):
    #'Sex', 'Age', 'Fare', 'Pclass', 'SibSp'
    Sexo = forms.IntegerField(label='Sex')
    Age = forms.IntegerField(label='Age')
    Fare = forms.FloatField(label='Fare')
    Pclass = forms.IntegerField(label='Pclass')
    SibSp = forms.IntegerField(label='SibSp')

