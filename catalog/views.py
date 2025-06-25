from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProductForm, ProductModeratorForm
from .models import Product, Category
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.core.cache import cache



from .services import ProductService


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        if self.request.user.has_perm('catalog.can_unpublish_product') and self.request.user.has_perm('catalog.delete_product'):
            return Product.objects.all()
        return Product.objects.filter(is_published=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = reverse_lazy('users:login')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    login_url = reverse_lazy('users:login')

    def get_success_url(self, **kwargs):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.delete_product'):
            return ProductModeratorForm
        return ProductForm

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user
        if product.owner != user and not user.has_perm('catalog.delete_product') :
            raise PermissionDenied
        return product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user
        if product.owner != user and not user.has_perm('catalog.delete_product') :
            raise PermissionDenied
        return product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductsByCategoryListView(ListView):
    model = Product
    template_name = 'catalog/products_by_category_list.html'

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return ProductService.get_products_by_category_cached(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs.get('pk'))
        # context['categories'] = Category.objects.all()
        return context
