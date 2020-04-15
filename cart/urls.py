from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
  path('', views.cart_view, name='order-summary'),
  path('add-to-cart/<slug:slug>/', views.add_to_cart_view, name='add-to-cart'),
]