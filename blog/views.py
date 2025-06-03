from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



from blog.models import Article


class BlogView(TemplateView):
    template_name = 'blog/main_page.html'


class BlogContactsView(TemplateView):
    template_name = 'blog/contacts.html'


class ArticleDetailView(DetailView):
    model = Article


class ArticlesListView(ListView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('blog:articles')
