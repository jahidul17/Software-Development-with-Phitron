from django.shortcuts import render,redirect
from .import forms
from album.models import Albums
# Create your views here.

def add_album(request):
    if request.method=='POST':
        album_form=forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        album_form=forms.AlbumForm()
    return render(request,'add_album.html',{'Form_album':album_form})


def edit_album(request,albumID):
    edit_alb=Albums.objects.get(pk=albumID)
    album_form=forms.AlbumForm(instance=edit_alb)
    # print(edit_alb.album_name)
    if request.method == 'POST':
        album_form=forms.AlbumForm(request.POST,instance=edit_alb)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request,'add_album.html',{'Form_album':album_form})


def delete_album(request,albumID):
    del_alb=Albums.objects.get(pk=albumID)
    del_alb.delete()
    return redirect('homepage')
