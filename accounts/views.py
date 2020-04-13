from django.shortcuts import render
from django.views.generic import CreateView, ListView

from accounts import forms
from accounts.models import Address


class UserRegistrationView(CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'


class AddressListView(ListView):
    model = Address
    template_name = 'accounts/address_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)