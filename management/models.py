from django.db import models

# Create your models here.
class Example(models.Model):
    name = models.CharField("Nombre", max_length=100)