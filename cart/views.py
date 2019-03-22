from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from products.models import Product


def view_cart(request):
    template= loader.get_template('cart.html')

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    context={'cart_items': cart_items, 'total': total, 'product_count': product_count}
    return HttpResponse(template.render(context,request))



def add_to_cart(request, id):

    

    cart = request.session.get('cart', {})

    

    request.session['cart'] = cart

    return redirect(reverse('index'))


def adjust_cart(request, id):

   
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity

    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

