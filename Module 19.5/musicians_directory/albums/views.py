from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages


# Create your views here.
def albums(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=forms.AlbumForm(request.POST)
            if form.is_valid():
                messages.success(request,'Album add Successfully')
                form.save()
        else:
            form=forms.AlbumForm()
        return render(request,'album.html',{'form':form})
    else:
        return redirect('login_page')
