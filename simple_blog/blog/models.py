from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    text = models.TextField(verbose_name='Текст', max_length=10000)
    created_time = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)

    def __str__(self):
        return self.title
