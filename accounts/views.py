from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy, reverse
from django.db.models import Q

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
# Create your views here.

User = get_user_model()


class UserDetailView(DeleteView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(
            self.request.user, self.get_object())
        context['following'] = following
        return context


class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            is_following = UserProfile.objects.toggle_follow(
                request.user, toggle_user)
        return redirect("profiles:detail", username=username)

# class UserFollowView(View):
#     def get(self, request, username, *args, **kwargs):
#         toggle_user = get_object_or_404(User, username__iexact=username)
#         if request.user.is_authenticated():
#             user_profile, created = UserProfile.objects.get_or_create(
#                 user=request.user)
#             if toggle_user in user_profile.following.all():
#                 user_profile.following.remove(toggle_user)
#             else:
#                 user_profile.following.add(toggle_user)

#         return redirect("profiles:detail", username=username)
