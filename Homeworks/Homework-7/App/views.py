from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):

    context = {}
    return render(request, 'home.html', context)


def products(request):
    products = Product.objects.all()
    
    context = {'products': products}
    return render(request, 'products.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {'product': product}
    return render(request, 'product_details.html', context)