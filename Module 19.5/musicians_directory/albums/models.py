from django.db import models
from musicians.models import Music


CHOICE =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

# Create your models here.
class Album(models.Model):
    album_name=models.CharField(max_length=50)
    release_date=models.DateTimeField(blank=True,null=True)
    rating=models.CharField(max_length=5,choices =CHOICE)
    music_author=models.ForeignKey(Music, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return f"{self.album_name} {self.release_date} {self.rating}"
