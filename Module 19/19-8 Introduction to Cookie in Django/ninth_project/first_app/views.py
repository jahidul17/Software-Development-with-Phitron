from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def home(request):
    response= render (request,'home.html')
    response.set_cookie('name','rahim')
    # response.set_cookie('name','karim',max_age=10)# after 10 sec delete. Base second like here 10 second
    
    # response.set_cookie('name','karim',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name=request.COOKIES.get('name')
    # print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response=render(request,'del.html')
    response.delete_cookie('name')
    return response






