from typing import Any
from django.shortcuts import render,redirect
from .import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from posts.models import Post


#for class base view
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views.generic import View


def register(request):
    usable_password = None
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type' : 'Register'})




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
                return redirect('profile')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})



@login_required  
def profile(request):
    # data=Post.objects.all()
    data=Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':data})




@login_required  
def edit_profile(request):
    if request.method=='POST':
        profile_form=forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form=forms.ChangeUserForm(instance=request.user)
    return render(request,'update_profile.html',{'form':profile_form})



def pass_change(request):
    if request.method=='POST':
         cpass_form=PasswordChangeForm(request.user,request.POST)
         if cpass_form.is_valid():
             cpass_form.save()
             messages.success(request,'Password Update Successfully')
             update_session_auth_hash(request,cpass_form.user)
             return redirect('profile')
    else:
        cpass_form=PasswordChangeForm(user=request.user)
    return render(request,'change_pass.html',{'form':cpass_form})    
 
 
 
def user_logout(request):
    logout(request)
    return redirect('user_login')
 
 
 
 
class UserLoginView(LoginView):
    template_name='register.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self,form):
        messages.success(self.request,'Logged in successful')
        return super().form_valid(form)
         
    def form_invalid(self,form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='login'
        return context
    



    