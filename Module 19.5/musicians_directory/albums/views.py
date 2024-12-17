from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from .import models


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
    
    
def edit_album(request,albumID):
    edit_alb=models.Album.objects.get(pk=albumID)
    album_form=forms.AlbumForm(instance=edit_alb)
    # print(edit_alb.album_name)
    if request.method == 'POST':
        album_form=forms.AlbumForm(request.POST,instance=edit_alb)
        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')
    return render(request,'album.html',{'form':album_form})


def delete_album(request,albumID):
    del_alb=models.Album.objects.get(pk=albumID)
    del_alb.delete()
    return redirect('home_page')
