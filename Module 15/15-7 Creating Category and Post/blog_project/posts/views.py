from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def add_post(request):
    if request.method == 'POST':#user post request koreche
        PostForm=forms.PostForm(request.POST)#user er post request data ekhane capture korlam
        if PostForm.is_valid():#post kora data valid ki na check kortechi
            PostForm.save() #jodi data valid hoy taile database e save hobe
            return redirect('add_post')#sod thik thakle thake add category ai url e pathie diba
        
    else: 
        PostForm=forms.PostForm()
    return render(request, 'add_post.html',{'form': PostForm})
 
 