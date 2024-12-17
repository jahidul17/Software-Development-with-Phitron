from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='add_post.html'
    success_url=reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class=forms.PostForm
    template_name='add_post.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile_page') 


@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name='delete.html'
    success_url=reverse_lazy('profile_page') 
    pk_url_kwarg='id'
    
    
@method_decorator(login_required,name='dispatch')
class DetailPostView(DetailView):
    model=models.Post
    pk_url_kwarg = 'id'
    template_name='post_details.html'
    
    
    def post(self,request,*args, **kwargs):
            comment_form=forms.CommentForm(data=self.request.POST)
            post=self.get_object()
            if comment_form.is_valid():
                new_comment=comment_form.save(commit=False)
                new_comment.post=post
                new_comment.save()
            return self.get(request,*args,**kwargs)        

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        post=self.object 
        comments=post.comments.all()
        comment_form = forms.CommentForm()            
        context['comments']=comments
        context['comment_form']=comment_form
        return context

