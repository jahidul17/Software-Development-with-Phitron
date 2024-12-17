from django.db import models
from categories.models import Brand
# from author.models import Author
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    image=models.ImageField(upload_to='upload/',blank=True,null=True)
    model=models.CharField(max_length=255,null=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    content=models.TextField()
    author=models.ManyToManyField(User,blank=True)
    
    def __str__(self) -> str:
        return self.model
    
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True) #jokhon ai class er object toiri hobe sei time rekhe dibe
    
    def __str__(self):
        return f"Comment by {self.name}"
