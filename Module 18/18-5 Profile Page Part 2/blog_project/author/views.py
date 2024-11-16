from django.shortcuts import render,redirect
from .import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _


# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form=forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
        
#     else: 
#         author_form=forms.AuthorForm()
#     return render(request, 'add_author.html',{'form': author_form})


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
    if request.method=='POST':
        profile_form=forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form=forms.ChangeUserForm(instance=request.user)
    return render(request,'profile.html',{'form':profile_form})



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
         