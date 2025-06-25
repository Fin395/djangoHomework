from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductsByCategoryListView
from django.views.decorators.cache import cache_page


app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='product_contacts'),
    path('<int:pk>/', cache_page(60 * 2)(ProductDetailView.as_view()), name='product_detail'),
    path('', ProductsListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:pk>/', ProductsByCategoryListView.as_view(), name='products_by_category_list'),

]