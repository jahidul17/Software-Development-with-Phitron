from django import forms
from django.forms.widgets import NumberInput   
import datetime
# from .models import MyModel

from django.db import models






class NameForm(forms.Form):
	name = forms.CharField()        
        
class CommentForm(forms.Form):
	comment = forms.CharField(widget=forms.Textarea)
 
class EmailForm(forms.Form):
	email = forms.EmailField()
 
class AgreeForm(forms.Form):
	agree = forms.BooleanField()
 
class DateForm(forms.Form):
	date = forms.DateField()
 

class BirthdateForm(forms.Form):
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
 
 
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']   
class Birthday_yearForm(forms.Form):
        birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))


# ----------------------------------------------------------------------
# Display Contact Page 

class ValueForm(forms.Form):
    value = forms.DecimalField()
    
class MessageForm(forms.Form):
    message = forms.CharField(max_length = 10,)
        

class DayForm(forms.Form):
	day = forms.DateField(initial=datetime.date.today)
 
 
 
 
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class choicesForm(forms.Form):
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    
    
    
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class RadioSelectForm(forms.Form):
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    
    
    
    
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class MultipleForm(forms.Form):
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    
    
    
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class CheckboxForm(forms.Form):
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    
    
    
# class ModelChoiceForm(forms.Form):
#     model_choice = forms.ModelChoiceField(
#         queryset = MyModel.objects.all(),
#         initial = 0
#         )
    
    
    
# class ModelMultipleChoiceForm(forms.Form):
#     model_choices = forms.ModelMultipleChoiceField(
#         widget = forms.CheckboxSelectMultiple,
#         queryset = MyModel.objects.all(),
#         initial = 0
#         )












