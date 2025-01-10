from django.db import models
from accounts.models import UserBankAccount
from .constants import TRANSACTION_TYPE

# Create your models here.
class Transaction(models.Model):
    account=models.ForeignKey(UserBankAccount,related_name='transactions',on_delete=models.CASCADE)#enjon user er multiple transaction hote pare
    amount=models.DecimalField(decimal_places=2,max_digits=12)
    balance_after_transaction=models.DecimalField(decimal_places=2,max_digits=12)
    transaction_type=models.IntegerField(choices=TRANSACTION_TYPE,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    loan_approve=models.BooleanField(default=False)
    is_bank_bankrupt = models.BooleanField(default=False, null=True, blank=True)
    
    class Meta:
        ordering=['timestamp'] #time er upor base kore sort korbo.



# class MoneyTransfer(models.Model):
#     sendmoney_account=models.ForeignKey(UserBankAccount, related_name='money_send', on_delete=models.CASCADE)
#     receivemoney_account=models.ForeignKey(UserBankAccount, related_name='money_receive', on_delete=models.CASCADE)
#     amount=models.DecimalField(decimal_places=2,max_digits=12,blank=True,null=True)
#     timestamp=models.DateField(auto_now_add=True,blank=True,null=True)
    

    
    

