from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]