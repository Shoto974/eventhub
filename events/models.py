from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    organization = models.CharField(max_length=100)


    def __str__(self):
        return self.title