from django.shortcuts import render

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
