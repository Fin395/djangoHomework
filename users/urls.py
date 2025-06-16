from django.urls import path
from users.apps import UsersConfig
from blog.views import BlogView, BlogContactsView, ArticleDetailView, ArticlesListView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('main/', BlogView.as_view(), name='article_main'),


]