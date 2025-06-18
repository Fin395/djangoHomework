from django import forms

from .mixins import StyleFormMixin
from .models import Product
from django.core.exceptions import ValidationError


FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['name'].widget.attrs.update({
    #         'class': 'form-control',  # Добавление CSS-класса для стилизации поля
    #         'placeholder': 'Введите наименование'  # Текст подсказки внутри поля
    #     })
    #
    #     self.fields['description'].widget.attrs.update({
    #         'class': 'form-control',  # Добавление CSS-класса для стилизации поля
    #         'placeholder': 'Введите описание'  # Текст подсказки внутри поля
    #     })
    #
    #     self.fields['image'].widget.attrs.update({
    #         'class': 'form-control',  # Добавление CSS-класса для стилизации поля
    #         'placeholder': 'Загрузите изображение'  # Текст подсказки внутри поля
    #     })
    #
    #     self.fields['category'].widget.attrs.update({
    #         'class': 'form-control'
    #     })
    #
    #     self.fields['price'].widget.attrs.update({
    #         'class': 'form-control',  # Добавление CSS-класса для стилизации поля
    #         'placeholder': 'Укажите цену'  # Текст подсказки внутри поля
    #     })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Слово {word} не может содержаться в наименовании продукта")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Слово '{word}' не может содержаться в описании продукта")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
                raise ValidationError("Цена не может быть отрицательной")
        return price
