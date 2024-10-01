from django.shortcuts import render
from . forms import contactForm



# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    if request.method=='POST':
        print(request.POST)
        email=request.POST.get('useremail')
        password=request.POST.get('userpass')
        select=request.POST.get('select')
        return render(request,'about.html',{'email':email,'password':password,'select':select})
    else:
        return render(request,'about.html')
        

def form(request):
        return render(request,'form.html')


def DjangoForm(request):
    form=contactForm(request.POST) #when use request.post than when submit data value is show
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'./first_app/django_form.html',{'form':form})

