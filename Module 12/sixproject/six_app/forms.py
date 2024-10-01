from django import forms

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



class StudentData(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    email=forms.EmailField()
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
    def clean(self):
        cleaned_data=super().clean()
        valname=self.cleaned_data['name']
        valemail=self.cleaned_data['email']
        if len(valname)<10:
            raise forms.ValidationError("Enter a name with at least 10 characters")
    
        if'.net' not in valemail:
            raise forms.ValidationError("Your email must contain .net")
