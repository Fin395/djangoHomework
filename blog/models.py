from django.db import models

class Article(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок блога",
    )
    content = models.TextField(
        verbose_name="Содержимое блога",
        help_text="Введите содержимое блога",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="previews/",
        blank=True,
        null=True,
        verbose_name="Превью блога",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"