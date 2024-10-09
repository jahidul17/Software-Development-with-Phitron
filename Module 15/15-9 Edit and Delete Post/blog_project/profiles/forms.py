from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__' #when i get all field from Author
        # fields=['name','bio'] #when i use specific field from Author
        # exclude =['bio'] #when i use without bio field
        
        