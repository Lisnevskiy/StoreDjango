from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request) -> object:
    if request.method == 'GET':
        return render(request, 'catalog/contacts.html')
    if request.method == 'POST':
        name: str = request.POST.get('name')
        phone: str = request.POST.get('phone')
        message: str = request.POST.get('message')
        print(name, phone, message)
        return render(request, 'catalog/contacts.html')


def product(request):
    product = Product.objects.get(name='Вишня')
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
