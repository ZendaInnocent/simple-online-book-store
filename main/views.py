from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView

from main import forms
from main.models import Product

class HomeView(TemplateView):
    template_name = 'main/home.html'

class AboutView(TemplateView):
    template_name = 'main/about.html'

class ContactView(FormView):
    form_class = forms.ContactForm
    template_name = 'main/contact.html'
    success_url = '/'

    def form_valid(self,form):
        form.send_mail()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'
    paginate_by = 2