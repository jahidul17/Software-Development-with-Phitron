from django.shortcuts import render
from first_app.forms import TestForm

# Create your views here.

def home(request):
    test=TestForm()
    return render(request,"home.html",{'form':test})

