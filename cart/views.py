from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from .models import Cart, Order


def cart_view(request):

  user = request.user

  carts = Cart.objects.filter(user=user)
  orders = Order.objects.filter(user=user, ordered=False)

  if carts.exists():
    order = orders[0]
    return render(request, 'cart/order_summary.html', {"carts": carts, 'order': order})
  
  else:
    messages.warning(request, "You do not have an active order")
    return redirect("products:product-list")

