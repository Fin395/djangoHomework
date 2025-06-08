from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='product_contacts'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductsListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]