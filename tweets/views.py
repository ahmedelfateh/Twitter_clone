from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Tweet

# Create your views here.


class TweetDetailView (DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    def get_object(self):
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)


class TweetListView (ListView):
    queryset = Tweet.objects.all()
    template_name = "tweets/list_view.html"
