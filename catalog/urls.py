from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('single_product/<int:pk>', views.single_product, name='single_product'),
    path('main_page/', views.main_page, name='main_page'),

]