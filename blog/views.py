from django.views.generic import TemplateView, DetailView

from blog.models import Article


class BlogView(TemplateView):
    template_name = 'blog/main_page.html'


class BlogContactsView(TemplateView):
    template_name = 'blog/contacts.html'


class ArticleDetailView(DetailView):
    model = Article
