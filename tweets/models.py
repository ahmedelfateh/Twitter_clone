from django.conf import settings
from django.db import models
from django.utils import timezone

from django.urls import reverse_lazy, reverse

from .validators import validate_content
# Create your models here.

# --------------------------------------Tweet


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(max_length=250, validators=[validate_content, ])
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk": self.pk})
