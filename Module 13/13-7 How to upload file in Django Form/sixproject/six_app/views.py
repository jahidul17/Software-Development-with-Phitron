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
    if request.method =='POST':
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            file=form.cleaned_data['file']
            with open('./six_app/upload/'+file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                              
            print(form.cleaned_data)
            return render(request,'./first_app/django_form.html',{'form':form})
    else:
        form=contactForm()
    return render(request,'./first_app/django_form.html',{'form':form})

  
