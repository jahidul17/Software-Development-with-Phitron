from django.shortcuts import render
# from albums.models import Album
from albums.models import Album

def home(request):
    data=Album.objects.all()
    return render(request,'home.html',{'data':data})

