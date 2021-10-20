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