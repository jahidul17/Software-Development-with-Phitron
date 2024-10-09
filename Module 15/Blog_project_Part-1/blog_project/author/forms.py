from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__' #when i get all field from Author
        # fields=['name','bio'] #when i use specific field from Author
        # exclude =['bio'] #when i use without bio field
        
        