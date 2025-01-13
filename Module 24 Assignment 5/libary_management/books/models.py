from django.db import models
from django.contrib.auth.models import User
from categories.models import BookCategory

# Create your models here.

class BookPost(models.Model):    
    title=models.CharField(max_length=255,null=True)
    image=models.ImageField(upload_to='upload/',blank=True,null=True)
    description=models.TextField(BookCategory,on_delete=models.CASCADE,null=True)
    price=models.IntegerField(null=True)
    category=models.ForeignKey()
    author=models.ManyToManyField(User,blank=True)

class Comment(models.Model):
    bookpost=models.ForeignKey(BookPost,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=25)
    email=models.EmailField(unique=True)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.name}"
