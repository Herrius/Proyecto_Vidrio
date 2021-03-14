from django import forms

class Valueform(forms.Form):
    busqueda = forms.CharField(max_length = 100)

#class RenewBookForm(forms.Form):
#    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    