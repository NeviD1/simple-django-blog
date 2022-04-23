from django.shortcuts import render
from rest_framework import generics
from blog.serializers import ArticleDetailSerializer


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleDetailSerializer

