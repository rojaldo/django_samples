from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()

class Hero(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
