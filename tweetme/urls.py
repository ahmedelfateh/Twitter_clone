"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from django.conf.urls.static import static
from django.conf import settings

from hashtags.views import HashTagView
from .views import home
from tweets.views import TweetListView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),  # /admin/
    url(r'^$', TweetListView.as_view(), name='home'),  # /home/
    url(r'^tweet/', include('tweets.urls', namespace='tweet')),  # + tweets.url
    # url(r'^profiles/', include('accounts.urls',
    #                            namespace='profiles')),  # + accounts.url
    url(r'^api/tweet/', include('tweets.api.urls',
                                namespace='tweet-api')),  # + tweets.api.urls
    url(r'^api/', include('accounts.api.urls',
                          namespace='profiles-api')),  # + tweets.api.urls
    url(r'^', include('accounts.urls',
                      namespace='profiles')),  # + accounts.url
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    # url(r'^hashtags/', include('hashtags.urls',
    #                            namespace='hashtags')),  # + hashtags.url
]

if settings.DEBUG:
    urlpatterns += (
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
