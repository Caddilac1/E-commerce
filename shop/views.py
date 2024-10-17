from django.shortcuts import render
from .models import *
import json
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
       # items = order.orderitem_set.all()
        cart_item = order.get_cart_items
    else:
        order = {'get_carttotal':0,'get_cart_items':0}
        items = []
        cart_item = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products,'order':order,'cart_item':cart_item}
    return render(request, 'store.html', context)




@login_required
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cart_item = order.get_cart_items
    context = {'items': items, 'order': order,'cart_item':cart_item}
    return render(request, 'cart.html', context)


@login_required
def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cart_item = order.get_cart_items
    context = {'items': items, 'order': order,'cart_item':cart_item}
    return render(request, 'checkout.html', context)



@login_required
def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was updated', safe=False)
