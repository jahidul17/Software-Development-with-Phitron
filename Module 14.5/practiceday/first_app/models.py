from django.db import models

# Create your models here.
# class StudentModel(models.Model):
#     roll=models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=30)
#     address=models.TextField()
    

class MyModel(models.Model):
    file_field = models.FileField(upload_to='files/')
    
class ImgModel(models.Model):
    image_field = models.ImageField(upload_to='images/')

    

