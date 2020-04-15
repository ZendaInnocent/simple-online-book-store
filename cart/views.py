from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from cart.models import Cart, Order
from products.models import Product


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


def add_to_cart_view(request, slug):
  item = get_object_or_404(Product, slug=slug)
  order_item, created = Cart.objects.get_or_create(
    item=item,
    user=request.user,
  )
  order_qs = Order.objects.filter(user=request.user, ordered=False)

  if order_qs.exists():
    order = order_qs[0]
    # check if the order item is in the order
    if order.order_items.filter(item__slug=item.slug).exists():
      order_item.quantity += 1
      order_item.save()
      messages.info(request, "This item quantity was updated")
      return redirect(reverse('products:product-detail', kwargs={'slug': slug}))

    else:
      order.order_items.add(order_item)
      messages.info(request, "This item was added to your cart.")
      return redirect('products:product-detail', kwargs={'slug':slug})
    
  else:
    order = Order.objects.create(user=request.user)
    order.order_items.add(order_item)
    messages.info(request, "This item was added to your cart.")
    return redirect('product:product-detail', kwargs={'slug':slug})
