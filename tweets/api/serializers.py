from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializers
from tweets.models import Tweet


class TweetModelSerializers(serializers.ModelSerializer):
    user = UserDisplaySerializers(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp)
