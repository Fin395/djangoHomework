from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductDetailView, ContactsView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('single_product/<int:pk>/', ProductDetailView.as_view(), name='single_product'),
    path('main_page/', ProductsListView.as_view(), name='main_page'),
    path('create/', ProductCreateView.as_view(), name='product_create'),

]