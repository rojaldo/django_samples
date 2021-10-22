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

    def __str__(self):
        return self.title + ' - ' + self.date + ' - ' + self.media_type + ' - ' + self.copyright + ' - ' + self.explanation

class Beer(models.Model):
    name = models.CharField(max_length=120)
    tagline = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    abv = models.FloatField()
    first_brewed = models.CharField(max_length=20)
    image_url = models.URLField(max_length=100)

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