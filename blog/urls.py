from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogView, BlogContactsView, ArticleDetailView, ArticlesListView, ArticleCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/main_page/', BlogView.as_view(), name='main_page'),
    path('blogs/contacts/', BlogContactsView.as_view(), name='contacts'),
    path('blogs/article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('blogs/articles/', ArticlesListView.as_view(), name='articles'),
    path('blogs/new/', ArticleCreateView.as_view(), name='new'),

]