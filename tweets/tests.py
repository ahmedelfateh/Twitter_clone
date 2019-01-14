from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tweet

# Create your tests here.

User = get_user_model()


class TweetModelTestCase(TestCase):

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user=User.objects.create(username='NoOne1'),
            content="random content for test purpose"
        )
        self.assertTrue(obj.content == "random content for test purpose")
        self.assertTrue(obj.id == 1)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user=User.objects.create(username='NoOne2'),
            content="random content for test purpose"
        )
        absolute_url = reverse("tweet:detail", kwargs={"pk": obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
