# from django.db import models
# from django.conf import settings

# from accounts.models import UserProfile


# class UserProfileManager(models.Manager):
#     use_for_related_fields = True

#     def all(self):
#         qs = self.get_queryset().all()
#         try:
#             if self.instance:
#                 qs = qs.exclude(user=self.instance)
#         except:
#             pass
#         return qs

#     def toggle_follow(self, user, to_toggle_user):
#         user_profile, created = UserProfile.objects.get_or_create(
#             user=user)  # (user_obj, true)
#         if to_toggle_user in user_profile.following.all():
#             user_profile.following.remove(to_toggle_user)
#             added = False
#         else:
#             user_profile.following.add(to_toggle_user)
#             added = True
#         return added

#     def is_following(self, user, followed_by_user):
#         user_profile, created = UserProfile.objects.get_or_create(user=user)
#         if created:
#             return False
#         if followed_by_user in user_profile.following.all():
#             return True
#         return False
