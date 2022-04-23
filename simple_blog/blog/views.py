from django.shortcuts import get_object_or_404
from rest_framework import generics
from blog.serializers import *


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleDetailSerializer


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentDetailSerializer

    def perform_create(self, serializer):
        kwargs = {}
        kwargs['article'] = get_object_or_404(Article, pk=self.kwargs['article_id'])
        if 'parent_id' in self.kwargs:
            kwargs['parent'] = get_object_or_404(Comment, pk=self.kwargs['parent_id'])
        serializer.save(**kwargs)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):

        def get_queryset_for_article(article_id, number_levels=3):
            return Comment.objects.filter(article__id=article_id).filter(path__len__lte=number_levels - 1)

        def get_queryset_for_comment(article_id, parent_id):
            return Comment.objects.filter(article__id=article_id).filter(path__overlap=[parent_id])

        article_id = self.kwargs['article_id']
        if 'parent_id' in self.kwargs:
            return get_queryset_for_comment(article_id, self.kwargs['parent_id'])
        else:
            return get_queryset_for_article(article_id)
