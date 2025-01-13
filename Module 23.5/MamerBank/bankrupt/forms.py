from django import forms
from .models import Bankrupt

class BankruptForm(forms.ModelForm):
    class Meta:
        model = Bankrupt
        fields = ['is_bankrupt']

