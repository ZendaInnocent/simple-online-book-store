from django.urls import path, include

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.UserRegistrationView.as_view(), name='signup'),
    path('addresses/create/', views.AddressCreateView.as_view(), name='address-create'),
    path('addresses/', views.AddressListView.as_view(), name='address-list'),
]