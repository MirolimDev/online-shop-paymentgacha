from django.urls import path

from .views import *

urlpatterns = [ 
    path('add_to_cart/', add_to_cart, name='add-to-cart'),
    path('delete_cart/', delete_cart, name='delete_cart'),
    path('delete_from_cart/', delete_from_cart, name='delete_from_cart'),
    path('checkout/', checkout, name='checkout'),
]