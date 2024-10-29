from django.shortcuts import render,redirect
from .import forms
from musician.models import Musicians

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musician_form=forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form=forms.MusicianForm()
    return render(request,'add_musician.html',{'form': musician_form})

def edit_musician(request,musID):
    edit_mus=Musicians.objects.get(pk=musID)
    musician_form=forms.MusicianForm(instance=edit_mus)
    
    if request.method == 'POST':
        musician_form=forms.MusicianForm(request.POST,instance=musID)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    return render(request,'add_musician.html',{'form': musician_form})
