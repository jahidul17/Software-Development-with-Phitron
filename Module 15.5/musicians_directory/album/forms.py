from django import forms 
from .models import Albums 


class AlbumForm(forms.ModelForm):
    class Meta:
        model=Albums
        fields='__all__'
        # exclude=['release_date']
        



