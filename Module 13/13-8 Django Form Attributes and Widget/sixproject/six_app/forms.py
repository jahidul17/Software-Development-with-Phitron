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
