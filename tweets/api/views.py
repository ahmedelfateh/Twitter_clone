from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions

from .serializers import TweetModelSerializers

from tweets.models import Tweet


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializers

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all().order_by("-pk")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs
