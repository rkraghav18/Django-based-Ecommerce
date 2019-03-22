from django.shortcuts import render
from .models import Product
from django.template import loader
#from .models import Products

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def compare(request,name):
    name=Product.objects.filter(name=name)
    return render(request, "result.html", {"name": name})
 