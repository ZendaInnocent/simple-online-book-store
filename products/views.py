from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import Product


class ProductListView(ListView):
    queryset = Product.objects.active().order_by('-updated')
    template_name = 'products/product_list.html'
    paginate_by = 2


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'