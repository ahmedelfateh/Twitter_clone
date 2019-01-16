from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy, reverse
from django.db.models import Q

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

User = get_user_model()


class UserDetailView(DeleteView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))
