from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .forms import RegisterForm,ChangeUserData
# from .forms import forms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from posts.models import Post



def signup(request):
    usable_password = None
    if request.method == 'POST':
        register_form =RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('signup_page')    
    else:
        register_form =RegisterForm()
    return render(request, 'signup.html', {'form' : register_form, 'type' : 'Register'})
    


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile_page')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('signup_page')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form, 'type' : 'Login'})


def profile(request):
    data=Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':data})
    
    
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
        return render(request,'./pass_change.html',{'form':form})
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
    return render(request,'edit_profile.html',{'form':form})


