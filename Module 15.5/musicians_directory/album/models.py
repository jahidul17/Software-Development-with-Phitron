from django.db import models
from musician.models import Musicians


RATING_CHOICES = [
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
    ('5', 'Five'),
]
# Create your models here.
class  Albums(models.Model):
    album_name=models.CharField(max_length=20)
    musician_author=models.ForeignKey(Musicians, on_delete=models.CASCADE)
    release_date=models.TimeField()
    rating_field = models.CharField(max_length=1, choices=RATING_CHOICES)
    
    def __str__(self) -> str:
        return self.album_name
