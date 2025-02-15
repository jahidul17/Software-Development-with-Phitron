from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm


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
        return render(request,'accounts/signup.html',{'form':form})
    else:
        return redirect('profile_page')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                messages.success(request,'Logged In Successfully')
                name=form.cleaned_data['username']
                user_pass=form.cleaned_data['password']
                user=authenticate(username=name,password=user_pass) #check user form database               
                if user is not None:
                    login(request,user)
                    return redirect('profile_page')
            else:
                messages.info(request,'Login faild!')
            #     return redirect('home_page')
        
        else:
            form=AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form})
    else:
        return redirect('profile_page')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html',{'user':request.user})
    else:
        return redirect('login_page')
    
    
def user_logout(request):
    logout(request)
    messages.info(request,'Logged Out Successfully')
    return redirect('login_page')


def password_change(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user) #user er pass kora data automatic change hoe jabe.
                return redirect('profile_page')
        
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'accounts/pass_change.html',{'form':form})
    else:
        return redirect('login_page')
    
    
def edit_profile(request):
    if request.method=='POST':
        form=ChangeUserData(request.POST,instance=request.user)
        if form.is_valid():
            messages.success(request,'Accoutn Update Successfully')
            form.save(commit=True)
    else:
        form=ChangeUserData(instance=request.user)
    return render(request,'accounts/edit_profile.html',{'form':form})

