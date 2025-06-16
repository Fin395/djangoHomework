from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from blog.views import BlogView, BlogContactsView, ArticleDetailView, ArticlesListView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView
from users.views import RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),

]