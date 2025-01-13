from django.db import models

# Create your models here.

class BookCategory(models.Model):
    name=models.models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,null=True,blank=True)
    
    def __str__(self):
        return self.name

