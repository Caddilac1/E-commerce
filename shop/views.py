from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'store.html',context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.orderitem_set.all()  
    else:
        items = []
        order ={'get_carttotal':0}

    context = {
        'items': items, 'order': order
    }
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.orderitem_set.all()  
    else:
        items = []
        order ={'get_carttotal':0}

    context = {
        'items': items, 'order': order
    }
    return render(request,'checkout.html',context)


def update_item(request):
    data = json.loads(request.body)
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