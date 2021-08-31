from django.contrib import admin
from django.db.models.deletion import CASCADE
from .models import  Cart, Order, OrderProduct
# Register your models here.

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderProduct)