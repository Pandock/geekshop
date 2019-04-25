from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import Basket


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            product_list = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': product_list,
            'basket': basket,
        }

        return render(request, 'mainapp/product_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', content)


# def products(request, pk=None):
#     if pk:
#         category = get_object_or_404(ProductCategory, pk=pk)
#         product_list = Product.objects.filter(category=category.id)
#     else:
#         product_list = Product.objects.all()
#
#     context = {'products': product_list}
#
#     product = ProductCategory.objects.all()
#     prod = {'product': product}
#     return render(request, 'mainapp/products.html', prod)


def contact(request):
    return render(request, 'mainapp/contact.html')
