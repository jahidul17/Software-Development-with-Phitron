from django.shortcuts import render,redirect
from .import forms

# Create your views here.

def add_categori(request):
    if request.method=='POST':
        caterogi_form=forms.BookCategoriForm(request.POST)
        if caterogi_form.is_valid():
            caterogi_form.save()
            return redirect('add_categori')
    else:
        caterogi_form=forms.BookCategoriForm()
    return render(request,'add_categori.html',{'form':caterogi_form})



