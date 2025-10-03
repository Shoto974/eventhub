from django.conf import settings
from django.db import models

from participation.models import Participation


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

    def get_image_url(self):
        image = self.eventimage_set.first()
        return image.url if image else None

    def get_participations(self):
        return self.participation_set.all()




class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name="images")
    url = models.URLField()

    def __str__(self):
        return f"Image pour {self.event.title}"
