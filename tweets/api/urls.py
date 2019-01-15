"""tweet app API URL Configuration """

from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    TweetCreateAPIView,
    TweetListAPIView,
)

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', TweetListAPIView.as_view(), name='list'),  # /api/tweet/
    url(r'^create$', TweetCreateAPIView.as_view(),
        name='create'),  # api/tweet/create
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), #/tweet/detail/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/update/
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/delete/
]
