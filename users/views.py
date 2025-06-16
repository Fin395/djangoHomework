from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserRegistrationForm

class RegisterView(CreateView):
    form_class = CustomUserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('products:product_list')