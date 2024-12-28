from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import DepositForm,WithdrawForm,LoanRequestForm
from .constants import DEPOSIT,WITHDRAWAL,LOAN,LOAN_PAID
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db import Sum  

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
    

class DepositMoneyView(TransactionCreateMixin):
    form_class=DepositForm
    title="Deposit"
    
    #By default set value in backend when user visit Deposit form
    def get_initial(self):
        initial={'transaction_type':DEPOSIT}
        return initial
    
    # Is form valid like request.POST method if form valid
    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance += amount #user er kache 500 taka, ami doposit korlam 1000. total balance 1500tk.
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request,f"{amount} $ was deposited to your account successfully. ")
        return super().form_valid(form)
    
    
    
class WithdrawMoneyView(TransactionCreateMixin):
    form_class=WithdrawForm
    title="Withdraw Money"
    
    #By default set value in backend when user visit Deposit form
    def get_initial(self):
        initial={'transaction_type':DEPOSIT}
        return initial
    
    # Is form valid like request.POST method if form valid
    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance -= amount #user er kache 1500 taka, ami withdrewl korlam 1000. total balance 500tk.
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request,f"Successfully withdraw {amount} $ form your account. ")
        return super().form_valid(form)
    
    
    
class LoanRequestView(TransactionCreateMixin):
    form_class=LoanRequestForm
    title="Request for loan"
    
    #By default set value in backend when user visit Deposit form
    def get_initial(self):
        initial={'transaction_type':LOAN}
        return initial
    
    # Is form valid like request.POST method if form valid
    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        current_loan_count=Transaction.objects.filter(account=self.request.user.account,transaction_type=3,loan_approve=True).count() 
        #transaction_type=3 means loan field form constants
        if current_loan_count>=3:
            return HttpResponse("You have crossed your limits.")
    
        messages.success(self.request,f"Loan request for amount {amount} $ has been successfully sent to admin. ")
        return super().form_valid(form)


class TransactionReportView(LoginRequiredMixin,ListView):
    template_name=""
    model=Transaction
    balance=0
    
    def get_queryset(self):
        #jodi user kono type filter na kora taile tar total transaction report dekhabo.
        queryset=super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str=self.request.GET.get('start_date')
        end_date_str=self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date=datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date=datetime.strptime(end_date_str, "%Y-%m-%d").date()

            queryset=queryset.filter(timestamp_date_gte =start_date,timestamp_date_lte=end_date)
            #here timestamp is variable form model then date and then gte menas greaterthan, lte means lessthan
       
            self.balance=Transaction.objects.filter(timestamp_date_gte =start_date,timestamp_date_lte=end_date).aggregate(sum('amount'))['amount__sum']
        else: 
            self.balance=self.request.user.account.balance
                   
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'account':self.request.user.account
        })
        return context

