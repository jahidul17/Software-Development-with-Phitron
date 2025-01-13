from django.db import models

# Create your models here.

class Bankrupt(models.Model):
    is_bankrupt = models.BooleanField(default=False)
    class meta
