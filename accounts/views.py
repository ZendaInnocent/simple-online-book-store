from django.shortcuts import render
from django.views.generic import CreateView

from accounts import forms


class UserRegistrationView(CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'
