from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request) -> object:
    if request.method == 'GET':
        return render(request, 'catalog/contacts.html')
    if request.method == 'POST':
        name: str = request.POST.get('name')
        phone: str = request.POST.get('phone')
        message: str = request.POST.get('message')
        print(name, phone, message)
        return render(request, 'catalog/contacts.html')
