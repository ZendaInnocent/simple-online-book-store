from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

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


class AddressCreateView(CreateView):
    model = Address
    template_name = 'accounts/address_create.html'
    form_class = forms.AddressForm
    success_url = reverse_lazy('accounts:address-list')

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user
        return super().form_valid(form)