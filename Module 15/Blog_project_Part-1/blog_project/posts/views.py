from django.shortcuts import render,redirect
from . import forms
from . import models
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
 
 

def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    PostForm=forms.PostForm(instance=post)
    # print(post.title)
    if request.method == 'POST':#user post request koreche
        PostForm=forms.PostForm(request.POST,instance=post)#user er post request data ekhane capture korlam
        if PostForm.is_valid():#post kora data valid ki na check kortechi
            PostForm.save() #jodi data valid hoy taile database e save hobe
            return redirect('homepage')#sod thik thakle thake add category ai url e pathie diba
        
    return render(request, 'add_post.html',{'form': PostForm})
 

def delete_post(request, id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
    