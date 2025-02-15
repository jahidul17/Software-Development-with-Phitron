from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    usable_password = None #remove passwrord based authentication   
    
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'required'})) 

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']     
                   
        # help_texts={
        #     'username':None,
        #     'first_name':None,
        #     'last_name':None,
        #     'email':None,
        #     'Password':None,
        # }
     