from django import forms
from django.db import models
from first_app.models import MyModel   

class TestForm(forms.ModelForm):
    class Meta:
         model=MyModel
         fields='__all__'



