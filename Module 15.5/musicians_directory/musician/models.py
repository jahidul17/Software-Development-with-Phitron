from django.db import models


Instrument_choice = [
        ('G', 'Guiter'),
        ('T', 'Tom Tom'),
        ('D', 'Drum'),
        ('H', 'Harmonium'),
        ('P', 'Piano'),
]

# Create your models here.
class Musicians(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField (max_length=12)
    instrument=models.TextChoices
    select_ins = models.CharField(max_length=1, choices=Instrument_choice)

    def __str__(self) -> str:
        return self.first_name

