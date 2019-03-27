from django.shortcuts import render
from .models import Product,Cart
from django.template import loader
#from .models import Products

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def compare(request,name):
    name=Product.objects.filter(name=name)
    return render(request, "result.html", {"name": name})


def buy(request,id):
    details = Product.objects.filter(id=id)
    return render(request, "payment.html", {"details": details})

def add_cart(request,id):
    user_name=request.POST.get("user_name")
    insert=Cart.objects.create(p_id=id,user_name=user_name)
    insert.save()
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

   # user_name=request.POST.get("username")



