from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogView, BlogContactsView, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/main_page/', BlogView.as_view(), name='main_page'),
    path('blogs/contacts/', BlogContactsView.as_view(), name='contacts'),
    path('blogs/article/', ArticleDetailView.as_view(), name='article'),

]