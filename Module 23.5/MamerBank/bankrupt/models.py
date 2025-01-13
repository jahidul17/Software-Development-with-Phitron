from django.db import models
from django.db.models import Model

# Create your models here.
class Bankrupt(Model):
    is_bankrupt = models.BooleanField(default=False)


