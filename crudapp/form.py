from django import forms
from .models import Home_card
from django.forms import fields
from django import forms

class ImageHomeForm(forms.ModelForm):
    
    class Meta:
        model = Home_card
        fields = ['title','image']
        




