from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Skystore'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request) -> object:
    context = {
        'title': 'Контакты'
    }
    if request.method == 'GET':
        return render(request, 'catalog/contacts.html', context)
    if request.method == 'POST':
        name: str = request.POST.get('name')
        phone: str = request.POST.get('phone')
        message: str = request.POST.get('message')
        print(name, phone, message)
        return render(request, 'catalog/contacts.html', context)


def products(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'product': product_item,
        'title': product_item.name
    }
    return render(request, 'catalog/product.html', context)
