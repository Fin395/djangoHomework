from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogView, BlogContactsView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blog'),
    path('blogs/contacts/', BlogContactsView.as_view(), name='contacts'),

]