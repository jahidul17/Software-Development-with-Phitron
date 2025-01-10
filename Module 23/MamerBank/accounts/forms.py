from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import Account_Type,Gender_Type
from django.contrib.auth.models import User
from .models import UserAddress,UserBankAccount


#here UserCreationForm use for built in model form + user creation attribute show into form  (3 model combine here)
class UserRegistrationForm(UserCreationForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'})) #here widget use for show calender into user
    gender=forms.ChoiceField(choices=Gender_Type)
    account_type=forms.ChoiceField(choices=Account_Type)
    street_address=forms.CharField()
    city=forms.CharField()
    postal_code=forms.IntegerField()
    country=forms.CharField()
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email','account_type','birth_date','gender','postal_code','country','city','street_address']
    
    #Like form.save()
    def save(self,commit=True):
        our_user=super().save(commit=False) #database e data save korbe na akhon
        if commit==True:
            our_user.save() #user model e data save korlam
            account_type=self.cleaned_data.get('account_type')
            gender=self.cleaned_data.get('gender')
            postal_code=self.cleaned_data.get('postal_code')
            city=self.cleaned_data.get('city')
            birth_date=self.cleaned_data.get('birth_date')
            country=self.cleaned_data.get('country')
            street_address=self.cleaned_data.get('street_address')

            UserAddress.objects.create(
                user=our_user,
                postal_code=postal_code,
                country=country,
                city=city,
                street_address=street_address
            )
            UserBankAccount.objects.create(
                user=our_user,
                account_type=account_type,
                gender=gender,
                birth_date=birth_date,
                account_no=100000+our_user.id, #optional
                
            )
        return our_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            # print(field)
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })





# profile ki ki jinis update korte parbe amader user

class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=Gender_Type)
    account_type = forms.ChoiceField(choices=Account_Type)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserBankAccount.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['account_type'].initial = user_account.account_type
                self.fields['gender'].initial = user_account.gender
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserBankAccount.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            user_address, created = UserAddress.objects.get_or_create(user=user) 

            user_account.account_type = self.cleaned_data['account_type']
            user_account.gender = self.cleaned_data['gender']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()

            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()

        return user
