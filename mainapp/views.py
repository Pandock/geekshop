from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):

    product = ProductCategory.objects.all()
    prod = {'product': product}
    return render(request, 'mainapp/products.html', prod)


def contact(request):
    return render(request, 'mainapp/contact.html')
