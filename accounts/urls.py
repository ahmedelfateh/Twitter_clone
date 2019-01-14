"""accounts URL Configuration """

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # url(r'^admin/', admin.site.urls, name='admin'), # /admin/
    # url(r'^$', TweetListView.as_view(), name='home'), # /home/ = http://127.0.0.1:8000
    # url(r'^tweet/', include('tweets.urls', namespace='tweet')), # + tweets.url
    # url(r'^api/tweet/', include('tweets.api.urls', namespace='tweet-api')), # + tweets.api.urls
]
