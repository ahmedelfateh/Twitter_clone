from django import forms
from django.forms.utils import ErrorList


class UserNeededMixin(object):

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(UserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
                ['user must be logged in'])
            return self.form_invalid(form)


class UserOwnerMixin(object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
                ['Must be the same user'])
            return self.form_invalid(form)
