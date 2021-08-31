from django.db import models
from django.db.models.fields import CharField
from django.utils.regex_helper import Choice
from catalog.models import Product
from django.contrib.auth.models import AnonymousUser, User
# Create your models here.

class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)





class Order(models.Model):
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20)
    amount = models.IntegerField()
    state = models.IntegerField(choices = [
        (1, "To'lov kutulmoqda"),
        (2, "To'lov bajarildi"),
        (3, "Buyurtma bekor qiilindi"),
        (4, "Buyurtma yetkazildi")], default=1
    )


class OrderProduct(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
