from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def add_brand(request):
    if request.method == 'POST':
        category_form=forms.BrandForm(request.POST)
        if category_form.is_valid():
            category_form.save() 
            return redirect('add_brand')
    else: 
        category_form=forms.BrandForm()
    return render(request, 'add_brand.html',{'form': category_form})
