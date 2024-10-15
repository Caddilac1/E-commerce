from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
        cart_items = order.get_cart_items 
    else:
        items = []
        order ={'get_carttotal':0,'get_cart_items':0}
        cart_items = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products,'items': items, 'order': order,'cart_items':cart_items}
    return render(request,'store.html',context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
        cart_items = order.get_cart_items 
    else:
        items = []
        order ={'get_carttotal':0,'get_cart_items':0}
        cart_items = order['get_cart_items']

    context = {
        'items': items, 'order': order,'cart_items':cart_items
    }
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()  
    else:
        items = []
        order ={'get_carttotal':0}

    context = {
        'items': items, 'order': order
    }
    return render(request,'checkout.html',context)


def update_item(request):
    data = json.load(request.body)
    print("data",data)
    product_id = data['productId']
    action = data['action']
    print("Action",action)
    print("productId",product_id)
    if request.user.is_authenticated:

        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        orderitems, created = OrderItem.objects.get_or_create(customer=customer, order=order)
        if action == "add":
            orderitems.quantity = (orderitems.quantity + 1)
            orderitems.save()
        elif action == "remove":
            orderitems.quantity = (orderitems.quantity - 1)
            if orderitems.quantity <= 0:
                orderitems.delete()
                orderitems.save()
    else:
        print("User is not logged in ...")
        print("Register to add items to cart ...")
    return JsonResponse("Item was added successfully .....  ",safe=False)