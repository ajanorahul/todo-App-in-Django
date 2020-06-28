from django import forms
from django.forms import ModelForm

from .models import App

class AppForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Add new Todo..'}))

    class Meta:
        model = App
        fields = '__all__'
