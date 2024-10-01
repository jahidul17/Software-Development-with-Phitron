from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    if request.method=='POST':
        email=request.POST.get('useremail')
        password=request.POST.get('userpass')
        return render(request,'about.html',{'email':email,'password':password})
    else:
        return render(request,'about.html',{'email':email,'password':password})
        

def form(request):
    if request.method=='POST':
        email=request.POST.get('useremail')
        password=request.POST.get('userpass')
        return render(request,'form.html',{'email':email,'password':password})
    else:
        return render(request,'form.html')
