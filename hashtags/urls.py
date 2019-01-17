"""hashtags app URL Configuration """

from django.conf.urls import url
from django.views.generic.base import RedirectView

# from .views import (
#     HashTagView,
# )

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    # url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),  # /hashtags/
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),  # /hashtags/create
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(),
    #     name='detail'),  # /hashtags/detail/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(),
    #     name='update'),  # /hashtags/update/
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(),
    #     name='delete'),  # /hashtags/delete/
]
