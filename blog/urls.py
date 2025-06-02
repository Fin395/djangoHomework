from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogView, BlogContactsView, ArticleView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blog'),
    path('blogs/contacts/', BlogContactsView.as_view(), name='contacts'),
    path('blogs/articles/', ArticleView.as_view(), name='articles'),

]