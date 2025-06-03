from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'preview']

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog:article', kwargs={'pk': self.object.pk})

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles')
