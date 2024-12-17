from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages

# Create your views here.
def musicians(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=forms.MusicianForm(request.POST)
            if form.is_valid():
                messages.success(request,'Music add Succefully.')
                form.save()
        else:
            form=forms.MusicianForm()
        return render(request,'music.html',{'form':form})
    else:
        return redirect('login_page')
