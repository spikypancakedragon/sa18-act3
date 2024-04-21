from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})