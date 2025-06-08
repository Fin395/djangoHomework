from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:main_page')


class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:main_page')


class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:main_page')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
