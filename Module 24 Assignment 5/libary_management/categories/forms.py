from django import forms
from .models import BookCategori


class BookCategoriForm(forms.ModelForm):
    class Meta:
        model=BookCategori
        fields='__all__'
        
        