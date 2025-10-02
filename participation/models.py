from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint



# Create your models here.
class Participation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'event'], name='unique_participation')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.event}"
