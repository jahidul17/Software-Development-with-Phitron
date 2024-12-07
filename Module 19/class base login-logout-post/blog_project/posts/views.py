from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#class base
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator #for import login required



# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         post_form=forms.PostForm(request.POST)
#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save() 
#             return redirect('add_post')
        
#     else: 
#         post_form=forms.PostForm()
#     return render(request, 'add_post.html',{'form': post_form})
 
 
#  #class Based View
@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='add_post.html'
    success_url=reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
           
 
 
 
# @login_required
# def edit_post(request,id):
#     post=models.Post.objects.get(pk=id)
#     post_form=forms.PostForm(instance=post)
#     if request.method == 'POST':
#         post_form=forms.PostForm(request.POST,instance=post)
#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save() 
#             return redirect('homepage')
        
#     return render(request, 'add_post.html',{'form': post_form})


@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class=forms.PostForm
    template_name='add_post.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile') 
 


# login_required
# def delete_post(request, id):
#     post=models.Post.objects.get(pk=id)
#     post.delete()
#     return redirect('homepage')



@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    # form_class=forms.PostForm
    template_name='delete.html'
    success_url=reverse_lazy('profile') 
    pk_url_kwarg='id'

    