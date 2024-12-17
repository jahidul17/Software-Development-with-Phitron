from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

#When create user form and model then create makemigrations and migrate and superuser
class RegisterForm(UserCreationForm):
    usable_password = None #remove passwrord based authentication   
    
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'required'})) 

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']     

     
#Edit user profile    
class ChangeUserData(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']