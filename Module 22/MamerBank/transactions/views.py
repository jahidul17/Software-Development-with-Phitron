from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction


# Create your views here.
# ei view ke inherit kore amrea deposite,withdraw,loan request er kaj korbo.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name=''
    model=Transaction
    title=''
    success_url=''
    
    #Return the keyword arguments for instantiating the form.
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update({
            'account':self.request.user.account,# je user request korse tar account.
        })
        return kwargs
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title':self.title
        }) 
        return context
    

