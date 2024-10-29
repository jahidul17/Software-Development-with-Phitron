from django.db import models
from taskcategory.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    assign_date=models.DateTimeField(auto_now=True)
    is_completed=models.BooleanField(default=False)
    task_cate=models.ManyToManyField(CategoryModel)
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    

