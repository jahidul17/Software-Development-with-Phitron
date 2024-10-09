from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def add_category(request):
    if request.method == 'POST':#user post request koreche
        category_form=forms.CategoryForm(request.POST)#user er post request data ekhane capture korlam
        if category_form.is_valid():#post kora data valid ki na check kortechi
            category_form.save() #jodi data valid hoy taile database e save hobe
            return redirect('add_category')#sod thik thakle thake add category ai url e pathie diba
        
    else: 
        category_form=forms.CategoryForm()
    return render(request, 'add_category.html',{'form': category_form})
 
 