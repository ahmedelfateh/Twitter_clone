from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.db.models import Q

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
    template_name = "tweets/create_view.html"
    login_url = "/admin/"
    form_class = TweetModelForm


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    # success_url = "/tweet"
    template_name = "tweets/update_view.html"
    login_url = "/admin/"


class TweetDeleteView(LoginRequiredMixin, UserNeededMixin, DeleteView):
    queryset = Tweet.objects.all()
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy('home')
    login_url = "/admin/"


class TweetDetailView (DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    def get_object(self):
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)


class TweetListView (ListView):
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    # queryset = Tweet.objects.all()
    # template_name = "tweets/list_view.html"
    # Revers tweets TEST

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context["create_form"] = TweetModelForm()
        context["create_url"] = reverse_lazy("tweet:create")
        return context
