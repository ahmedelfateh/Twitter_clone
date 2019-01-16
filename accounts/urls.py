"""accounts URL Configuration """
from django.conf.urls import url
from django.views.generic.base import RedirectView

from django.views.generic.base import RedirectView

from .views import (
    UserDetailView, )

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    # url(r'^search/$', TweetListView.as_view(), name='list'),  # /profiles/
    # url(r'^create/$', TweetCreateView.as_view(),
    #     name='create'),  # /profiles/create
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(),
        name='detail'),  # /profiles/detail/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(),
    #     name='update'),  # /profiles/update/
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(),
    #     name='delete'),  # /profiles/delete/
]
