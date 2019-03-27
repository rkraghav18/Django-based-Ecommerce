from django.conf.urls import url, include
from django.urls import path
from .views import all_products,compare,buy

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^compare/(?P<name>.+?)/$', compare, name='compare'),
    url(r'^buy/(?P<id>.+?)/$',buy, name='buy'),
    ]