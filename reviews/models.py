from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from events.models import Event


# Create your models here.
class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return f"Review de {self.user.username} sur {self.event}"


class ReviewMedia(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    url = models.URLField()
    media_type  = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image pour {self.review.user.username} - {self.review.event.title}"
