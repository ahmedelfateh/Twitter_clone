"""tweet app URL Configuration """

from django.conf.urls import url
from django.views.generic.base import RedirectView

from django.views.generic.base import RedirectView

from .views import (TweetListView, TweetDetailView,
                    TweetCreateView, TweetUpdateView,
                    TweetDeleteView, RetweetView,)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListView.as_view(), name='list'),  # /tweet/
    url(r'^create/$', TweetCreateView.as_view(), name='create'),  # /tweet/create
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(),
        name='detail'),  # /tweet/detail/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(),
        name='detail'),  # /tweet/1/# /tweet/retweet/
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(),
        name='update'),  # /tweet/update/
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(),
        name='delete'),  # /tweet/delete/
]
