from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = 'blog/main_page.html'


class BlogContactsView(TemplateView):
    template_name = 'blog/contacts.html'


class ArticleView(TemplateView):
    template_name = 'blog/blog_list.html'