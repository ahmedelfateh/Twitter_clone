from django.contrib import admin

from .models import Tweet
from .forms import TweetModelForm

from .forms import TweetModelForm

# Register your models here.


class TweetModeladmin(admin.ModelAdmin):
    form = TweetModelForm

    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetModeladmin)
