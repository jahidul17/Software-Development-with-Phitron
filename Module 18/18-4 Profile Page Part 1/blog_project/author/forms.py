from django import forms
# from .models import Author

from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model=Author
#         fields='__all__' #when i get all field from Author
#         # fields=['name','bio'] #when i use specific field from Author
#         # exclude =['bio'] #when i use without bio field
        
        
        
class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        
        
class ChangeUserForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
      
        
        
        
        
        