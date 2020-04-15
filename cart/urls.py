from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
  path('', views.cart_view, name='order-summary'),
  path('add-to-cart/<slug:slug>/', views.add_item_to_cart, name='add-to-cart'),
  path('remove-from-cart/<slug:slug>/', views.remove_item_from_cart, name='remove-from-cart'),
]