from django.urls import path
from blog.views import *


app_name = 'blog'
urlpatterns = [
    path('article/create/', ArticleCreateView.as_view()),
    path('article/<int:article_id>/comments/', CommentListView.as_view()),
    path('article/<int:article_id>/comments/create/', CommentCreateView.as_view()),
    path('article/<int:article_id>/comments/<int:parent_id>/comments/', CommentListView.as_view()),
    path('article/<int:article_id>/comments/<int:parent_id>/comments/create/', CommentCreateView.as_view()),
]
