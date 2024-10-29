from django.shortcuts import render
from album.models import Albums
# from musician.models import Musicians


def home(request):
    # mus=Musicians.objects.all()
    # print(mus)
    info=Albums.objects.all()
    print(info)
    return render(request,'home.html',{'data':info})