from typing import Any

from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


class ProductService:

    @staticmethod
    def get_products_by_category(category_id: int) -> Any:
        """ Возвращает QuerySet (продукты) по идентификатору категории """
        products = Product.objects.filter(category_id=category_id)
        if not products.exists():
            return None
        return products

    @staticmethod
    def get_products_by_category_cached(category_id: int) -> Any:
        """ Проверяет подключение кеширования и в положительном случае возвращает QuerySet из кеша """
        if not CACHE_ENABLED:
            return ProductService.get_products_by_category(category_id)
        queryset = cache.get('products_by_category')
        if not queryset:
                queryset = ProductService.get_products_by_category(category_id)
                cache.set('products_by_category', queryset, 60 * 2)
        return queryset
