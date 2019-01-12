from .views import (TweetListView, TweetDetailView,
                    TweetCreateView, TweetUpdateView,
                    TweetDeleteView, )
"""tweet app URL Configuration """

from django.conf.urls import url
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListView.as_view(), name='search'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
