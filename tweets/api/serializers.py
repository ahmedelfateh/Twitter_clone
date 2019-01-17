from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializers
from tweets.models import Tweet


class TweetModelSerializers(serializers.ModelSerializer):
    user = UserDisplaySerializers(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    is_retweet = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'is_retweet',
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp)

    def get_is_retweet(self, obj):
        if obj.parent:
            return str("")
        return str("Retweet")
