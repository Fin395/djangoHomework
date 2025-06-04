from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogView, BlogContactsView, ArticleDetailView, ArticlesListView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('main/', BlogView.as_view(), name='article_main'),
    path('contacts/', BlogContactsView.as_view(), name='article_contacts'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticlesListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

]