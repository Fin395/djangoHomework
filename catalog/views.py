from django.shortcuts import render, get_object_or_404
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
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)


def main_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/main_page.html', context)


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('Наименование продукта')
        description = request.POST.get('Описание продукта')
        image = request.POST.get('Изображение продукта')
        category = request.POST.get('Категория продукта')
        price = request.POST.get('Цена продукта')
         = request.POST.get('Дата создания продукта')
        updated_at = request.POST.get('Дата последнего изменения')
        Product.objects.create(name=name, description=description, category=category, price=price)
        return HttpResponse("Спасибо! Товар успешно создан!")
    return render(request, 'catalog/create_product.html')