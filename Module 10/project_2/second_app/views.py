from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     # return HttpResponse("This is home page.")
#     return render()

def home(request):
    return render(request, 'second_app/home.html')



