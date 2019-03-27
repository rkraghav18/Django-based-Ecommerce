from django.conf.urls import url, include
from django.urls import path
from .views import all_products,compare,buy,add_cart

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^compare/(?P<name>.+?)/$', compare, name='compare'),
    url(r'^buy/(?P<id>.+?)/$',buy, name='buy'),
    url(r'^add_cart/(?P<id>.+?)/$', add_cart, name='add_cart'),
    ]