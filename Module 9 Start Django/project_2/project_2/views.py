from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is project----- home page.")

# E:\Phitron\Software Development Project\Module 9 Start Django\project_2\templates
def index(request):
    return render(request,'index.html')