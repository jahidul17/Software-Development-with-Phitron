from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
 

# Create your views here.
def home(request):
    return render(request, './home.html')


def signup(request):
    if not request.user.is_authenticated:        
        if request.method=='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account createrd Successfully')
                messages.warning(request,'Warning')
                messages.info(request,'Info')
                form.save(commit=True)
                print(form.cleaned_data)
        else:
            form=RegisterForm()       
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        
        if request.method == 'POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user=authenticate(username=name,password=userpass)#check kortechi user database e ache kina
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form=AuthenticationForm()
        return render(request,'./login.html',{'form':form})
    
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request,'./profile.html',{'user':request.user})
    else:
        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')
    

