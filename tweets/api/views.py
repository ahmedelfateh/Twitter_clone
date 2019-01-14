from rest_framework import generics

from .serializers import TweetModelSerializers

from tweets.models import Tweet


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializers

    def get_queryset(self):
        return Tweet.objects.all()
