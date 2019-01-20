import re
from django.conf import settings
from django.db import models
from django.utils import timezone

from django.urls import reverse_lazy, reverse

from django.db.models.signals import post_save
from hashtags.signals import parsed_hashtags

from .validators import validate_content
# --------------------------------------inline Manager


class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        qs = self.get_queryset().filter(
            user=user, parent=og_parent
        ).filter(
            timestamp__year=timezone.now().year,
            timestamp__month=timezone.now().month,
            timestamp__day=timezone.now().day,
        )
        if qs.exists():
            return None

        obj = self.model(
            parent=og_parent,
            user=user,
            content=parent_obj.content,
        )
        obj.save()

        return obj
# --------------------------------------Tweet


class Tweet(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(max_length=250, validators=[validate_content, ])
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    objects = TweetManager()

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-timestamp']

# --------------------------------------Signal


def post_save_tweet_receiver(sender, instance, created, *args, **kwargs):
    if created and not instance.parent:
        user_regex = r'@(?P<username>[\w.@+-]+)'
        username = re.findall(user_regex, instance.content)

        hashtag_regex = r'#(?P<hashtag>[\w\d-]+)'
        hashtag = re.findall(hashtag_regex, instance.content)
        parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtag)


post_save.connect(post_save_tweet_receiver, sender=Tweet)
