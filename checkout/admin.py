from django.contrib import admin

# Register your models here.
from .models import Order,OrderLineItem

admin.site.register(Order)
admin.site.register(OrderLineItem)
