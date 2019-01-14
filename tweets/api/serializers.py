from rest_framework import serializers


from accounts.api.serializers import UserDisplaySerializers
from tweets.models import Tweet


class TweetModelSerializers(serializers.ModelSerializer):
    user = UserDisplaySerializers()

    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
        ]
