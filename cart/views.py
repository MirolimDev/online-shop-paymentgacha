

from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.shortcuts import render

from catalog.models import Product
from django.http import JsonResponse

from django.core.exceptions import ObjectDoesNotExist
from .models import Cart, OrderProduct

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order


@csrf_exempt
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))

    # product = Product.objects.all()
    carts = Cart.objects.filter(user_id = request.user.id)
    
    try:
        cart = Cart.objects.get(product_id=product_id)
        cart.quantity += quantity
        cart.save()

    except ObjectDoesNotExist:
        cart = Cart.objects.create(product_id=Product.objects.get(id=product_id), quantity=quantity, user_id = User.objects.get(id=request.user.id))
        cart.save()
     




    return render(request, 'cart_history.html', {
        'carts': carts
    })




@login_required(login_url='/accounts/login')
def checkout(request):

    order_form = OrderForm()
    # carts = Cart.objects.filter(user_id = request.user.id)
    # order_products = []

    # for cart in carts:

    #     product_sell = Product.objects.get(name=cart.product_id)
    #     order_products.append(product_sell)

    carts = Cart.objects.filter(user_id = request.user.id)

 


    if request.POST:
        order_form = OrderForm(request.POST)
        print('salom')
        if order_form.is_valid():
            print('xayr')
            order = Order()
            order.user_id = User.objects.get(id=2)
            order.phone = request.POST.get('phone')
            order.amount = 100000
            order.first_name = request.POST.get('first_name')
            order.last_name = request.POST.get('last_name')
            order.save()
            save_order_products(order, request)

            clear_cart(request)

            return redirect('index')

    return render(request, 'checkout.html',{
        'form': order_form,
        'total_amount': get_cart_total_amount(request),
        
        'carts': carts
    })



def get_cart_total_amount(request):

    carts = Cart.objects.filter(user_id = request.user.id)
    total_amount = 0

    for cart in carts:
        total_amount += cart.product_id.price * cart.quantity

    return total_amount



def clear_cart(request):
    carts = Cart.objects.filter(user_id = request.user.id)
    carts.delete()


def save_order_products(order, request):
    carts = Cart.objects.filter(user_id = request.user.id)

    for cart in carts:
        order_product = OrderProduct()
        order_product.product_id = cart.product_id
        order_product.quantity = cart.quantity
        order_product.order_id = order

        order_product.save()




@csrf_exempt
def delete_from_cart(request):
    product_id = request.POST.get('product_id')
    
    cart = Cart.objects.filter(product_id = product_id)
    cart.delete()
    # product = Product.objects.all()
    carts = Cart.objects.filter(user_id = request.user.id)
    
    return render(request, 'table_body.html', {
        'carts': carts
    })



@csrf_exempt
def delete_cart(request):

    product_id = request.POST.get('product_id')
    print(product_id)
    print(product_id)
    print(product_id)
    print(product_id)
    print(product_id)
    print(request.POST)
    cart = Cart.objects.filter(product_id = product_id)
    cart.delete()
    # product = Product.objects.all()
    carts = Cart.objects.filter(user_id = request.user.id)
    
    return render(request, 'cart_history.html', {
        'carts': carts
    })

  




