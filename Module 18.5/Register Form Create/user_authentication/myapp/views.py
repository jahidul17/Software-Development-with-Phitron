from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
# def home(request):
#     # return HttpResponse("This is my app.")
#     form=RegisterForm()
#     return render(request,'home.html',{'form':form})

def signup(request):
    # if not request.user.is_authenticated:
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account created successfully')
            form.save(commit=True)
            # print(form.cleaned_data) #for show submit data
    else:
        form=RegisterForm()
    return render(request,'home.html',{'form':form})
                