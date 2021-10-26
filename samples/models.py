from django.utils import timezone
from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()

class Hero(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

class NasaAPOD(models.Model):
    copyright = models.CharField(max_length=50, default='unknown')
    date = models.DateField()
    explanation = models.TextField()
    hdurl = models.URLField(max_length=100, default='')
    media_type = models.CharField(max_length=10)
    service_version = models.CharField(max_length=2)
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=100)


class Beer(models.Model):
    name = models.CharField(max_length=120)
    tagline = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    abv = models.FloatField()
    first_brewed = models.CharField(max_length=20)
    image_url = models.URLField(max_length=100)

# card model from opentdb
class MyTrivialCard(models.Model):
    question = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    difficulty = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    correct_answer = models.CharField(max_length=120)
    # get list of incorrect answers as a list
    incorrect_answers_1 = models.CharField(max_length=120)
    incorrect_answers_2 = models.CharField(max_length=120, default='')
    incorrect_answers_3 = models.CharField(max_length=120, default='')
    
class Post(models.Model):
   author = models.ForeignKey('auth.User',on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=200)
   text = models.TextField()
   created_date = models.DateTimeField(
           default=timezone.now)
   published_date = models.DateTimeField(
           blank=True, null=True)

   def publish(self):
       self.published_date = timezone.now()
       self.save()

   def __str__(self):
       return self.title

class Product(models.Model):
    name = models.CharField(max_length=130)
    description = models.TextField(blank=True)
    price = models.FloatField(blank=True)