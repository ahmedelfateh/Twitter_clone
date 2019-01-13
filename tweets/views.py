from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TweetModelForm
from .models import Tweet
from .mixin import UserNeededMixin, UserOwnerMixin

# Create your views here.


class TweetCreateView(LoginRequiredMixin, UserNeededMixin, CreateView):
    queryset = Tweet.objects.all()
    form = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = "/tweets"
    login_url = "/admin/"
    fields = [
        # 'user',
        'content'
    ]


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form = TweetModelForm
    success_url = "/tweets"
    template_name = "tweets/update_view.html"
    login_url = "/admin/"
    fields = [
        # 'user',
        'content'
    ]


class TweetDeleteView(LoginRequiredMixin, UserNeededMixin, DeleteView):
    queryset = Tweet.objects.all()
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy('list')
    login_url = "/admin/"


class TweetDetailView (DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    def get_object(self):
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)


class TweetListView (ListView):
    queryset = Tweet.objects.all()
    template_name = "tweets/list_view.html"
