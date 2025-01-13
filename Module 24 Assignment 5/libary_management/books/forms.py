from django import forms 
from .models import BookPost,Comment

class BookPostForm(forms.ModelForm):
    class Meta:
        model=BookPost
        exclude=['author']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']

