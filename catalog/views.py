from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваши данные успешно отправлены.")
    return render(request, 'catalog/contacts.html')


def single_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)


def main_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/main_page.html', context)