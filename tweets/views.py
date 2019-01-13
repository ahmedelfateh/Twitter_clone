from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .forms import TweetModelForm
from .models import Tweet

# Create your views here.


class TweetCreateView(CreateView):
    queryset = Tweet.objects.all()
    form = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = "/tweets"
    fields = [
        # 'user',
        'content'
    ]

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(TweetCreateView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class TweetDetailView (DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    def get_object(self):
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)


class TweetListView (ListView):
    queryset = Tweet.objects.all()
    template_name = "tweets/list_view.html"
