from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# --------------------------------------Tweet


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.content)
