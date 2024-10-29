from django.shortcuts import render

from first_app.forms import NameForm,CommentForm,EmailForm,AgreeForm,DateForm,BirthdateForm,Birthday_yearForm

from first_app.forms import ValueForm,MessageForm,DayForm,choicesForm,RadioSelectForm,MultipleForm,CheckboxForm
# ,ModelChoiceForm,ModelMultipleChoiceForm

from first_app.models import MyModel,ImgModel


# Create your views here.
def home(request):
    name=NameForm()
    comment=CommentForm()
    email=EmailForm()
    agree=AgreeForm()
    date=DateForm()
    birthdate=BirthdateForm()
    birthyear=Birthday_yearForm()
    return render(request,'home.html',{'name':name,'comment':comment,'email':email,'agree':agree,'date':date,'birthdate':birthdate,'birthyear':birthyear})

    

def contact(request):
    val=ValueForm()
    form=MessageForm()
    day=DayForm()
    choice1=choicesForm()
    choice2=RadioSelectForm()
    choice3=MultipleForm()
    choice4=CheckboxForm()
    # choice5=ModelChoiceForm()
    # choice6=ModelMultipleChoiceForm()
    mod=MyModel()
    imgmod=ImgModel()
    
    
    return render(request,'contact.html',{'val':val,'form':form,'day':day,'choice1':choice1,'choice2':choice2,'choice3':choice3,'choice4':choice4,'mod':mod,'imgmod':imgmod})
    # return render(request,'contact.html',{'val':val,'form':form,'day':day,'choice1':choice1,'choice2':choice2,'choice3':choice3,'choice4':choice4,'choice5':choice5,'choice6':choice6})
    

