from django import forms

class actionForm(forms.Form):
    texbox = forms.CharField(max_length=10)