from django import forms
from django.core import validators

# weidgets == field to html input
class contactForm(forms.Form):
    # name=forms.CharField(label="Full Name : ",initial="Rahim",help_text="Total length must be within 70 characters.",required=False,disabled=True,widget=forms.Textarea(attrs={'id':'text_area','Class':'Class1 class 2','placeholder':'Enter your name'}))
    name=forms.CharField(label="Full Name : ",help_text="Total length must be within 70 characters.",required=False,disabled=True,widget=forms.Textarea(attrs={'id':'text_area','Class':'Class1 class 2','placeholder':'Enter your name'}))
    file=forms.FileField()    
    
    email=forms.EmailField(label="User Email")
    age=forms.IntegerField(widget=forms.NumberInput)
    weight=forms.FloatField()
    balance=forms.DecimalField()
    check=forms.BooleanField()
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICE=[('S','Small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)
    MEAL=[('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza=forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)



# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.EmailField()
#     def clean_name(self):
#         valname=self.cleaned_data['name']
#         if len(valname)<10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")
#         return valname
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if'.net' not in valemail:
    #         raise forms.ValidationError("Your email must contain .net")
    # return valemail
        
        
    #Above function with in one function
    # def clean(self):
    #     cleaned_data=super().clean()
    #     valname=self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    
    #     if'.net' not in valemail:
    #         raise forms.ValidationError("Your email must contain .net")


def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter a value at least 10 chars")


class StudentData(forms.Form):
    name=forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,message='Enter a name with at max 10 charecters')])
    text=forms.CharField(widget=forms.TextInput,validators=[len_check])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid email")])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message="age must be maximum 34"),validators.MinValueValidator(20,message="age must be at least 20")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png','jpeg'],message="File extension must be ended with .pdf or .png or .jpeg")])
    
class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_pasword=forms.CharField(widget=forms.PasswordInput)
  
    def clean(self):
        cleaned_data=super().clean()
        val_pass=self.cleaned_data['password']
        val_conpass=self.cleaned_data['confirm_pasword']
        val_name=self.cleaned_data['name']
        if val_conpass!=val_pass:
            raise forms.ValidationError("Password dosen't match")
        if len(val_name)<15:
            raise forms.ValidationError("Name must be at least 15 characters")

        