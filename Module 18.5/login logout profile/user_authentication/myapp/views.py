from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
#     # return HttpResponse("This is my app.")
#     form=RegisterForm()
    return render(request,'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account created successfully')
                form.save(commit=True)
                # print(form.cleaned_data) #for show submit data
        else:
            form=RegisterForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('profile_page')
    


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                user_pass=form.cleaned_data['password']
                user=authenticate(username=name,password=user_pass) #check user form database               
                if user is not None:
                    login(request,user)
                    return redirect('profile_page')
            # else:
            #     return redirect('home_page')
        
        else:
            form=AuthenticationForm()
        return render(request,'./login.html',{'form':form})
    else:
        return redirect('profile_page')


def profile(request):
    if request.user.is_authenticated:
        return render(request, './profile.html',{'user':request.user})
    else:
        return redirect('login_page')
    
    
def user_logout(request):
    logout(request)
    return redirect('login_page')
     
   
            
            
            