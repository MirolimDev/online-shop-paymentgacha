from django.shortcuts import render, redirect
from .models import Category, Product, Slider
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    slider = Slider.objects.all()

    return render(request, 'index.html', {
        "categories": categories,
        "products": products,
        'sliders': slider
    })

def product_details(request, slug):
    categories = Category.objects.all()
    products = Product.objects.all()
    try:
        product = Product.objects.get(slug=slug)
        
        return render(request, 'product_detail.html', {'product': product, 'categories': categories, 'products': products})
    except ObjectDoesNotExist:
        pass
