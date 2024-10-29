from django.shortcuts import render,redirect
from .import forms
from taskmodel.models import TaskModel

# Create your views here.
def taskpage(request):
    if request.method=='POST':
        task_form=forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('showtask')
    
    else:
        task_form=forms.TaskForm()
    return render(request, 'taskmodel.html',{'task_form':task_form})


def edit_task(request, task_id):
    task=TaskModel.objects.get(pk=task_id)
    task_form=forms.TaskForm(instance=task)
    if request.method=='POST':
        task_form=forms.TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('showtask')
    return render(request, 'taskmodel.html',{'task_form':task_form})

    path('delete/<int:del_id>',views.delete_task, name='delete_task'),
def delete_task(request, del_id):
    del_task=TaskModel.objects.get(pk=del_id)
    del_task.delete()
    return redirect('showtask')