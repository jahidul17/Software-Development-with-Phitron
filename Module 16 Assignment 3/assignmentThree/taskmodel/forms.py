from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'        
        # exclude=["assign_date"]

        labels = {
            "titel": "Task Title",
            "description": "Task Description",
            "is_completed": "Task Status",
            "task_cate": "Task Category",
        }

        widgets = {
            "titel": forms.TextInput(
                attrs={"placeholder": "Task Title"}
            ),
            "description":forms.Textarea(attrs={"placeholder": "Write here Task Description","rows":4}),

        }