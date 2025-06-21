from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL, related_name='owner_products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [('can_unpublish_product', 'Can unpublish product')]
