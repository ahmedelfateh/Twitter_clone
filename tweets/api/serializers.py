from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializers
from tweets.models import Tweet


class ParentTweetModelSerializers(serializers.ModelSerializer):
    user = UserDisplaySerializers(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    # did_like = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'likes',
            # 'did_like',
        ]

    # def get_did_like(self, obj):
    #     request = self.context.get("request")
    #     user = request.user
    #     if user.is_authenticated():
    #         if user in obj.liked.all():
    #             return True
    #     return False

    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp)


class TweetModelSerializers(serializers.ModelSerializer):
    user = UserDisplaySerializers(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    parent_id = serializers.CharField(write_only=True, required=False)
    parent = ParentTweetModelSerializers(read_only=True)
    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'parent_id',
            'parent',
            'likes',
            'did_like',
            'reply',
        ]

    def get_did_like(self, obj):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated():
            if user in obj.liked.all():
                return True
        return False

    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp)
