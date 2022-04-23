from dataclasses import field
from rest_framework import serializers
from blog.models import Article


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['created_time']
