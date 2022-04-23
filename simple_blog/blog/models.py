from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    text = models.TextField(verbose_name='Текст', max_length=10000)
    created_time = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(verbose_name='Текст', max_length=1000)
    created_time = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительский комментарий')
    path = ArrayField(base_field=models.IntegerField(), blank=True, verbose_name='Путь до текущего комментария')

    class Meta:
        ordering = ['article', 'pk']
        indexes = [
            models.Index(fields=['article', 'path',]),
        ]

    def __str__(self):
        return self.text[:250]

    def save(self, *args, **kwargs):
        self.validate_comment()
        path = []
        if self.parent is not None:
            path = self.parent.path
            path.append(self.parent.pk)
        self.path = path
        super().save(*args, **kwargs)

    def validate_comment(self):
        article = self.article
        parent = self.parent
        if parent is not None and parent.article != article:
            raise ValidationError('Parent must belong to the same article')
