from django.urls import path
from blog.views import ArticleCreateView, CommentListToArticleView,\
    CommentCreateToArticleView, CommentListToCommentView, CommentCreateToCommentView


app_name = 'blog'
urlpatterns = [
    path('article/create/',
         ArticleCreateView.as_view()),
    path('article/<int:article_id>/comments/',
         CommentListToArticleView.as_view()),
    path('article/<int:article_id>/comments/create/',
         CommentCreateToArticleView.as_view()),
    path('article/<int:article_id>/comments/<int:parent_id>/comments/',
         CommentListToCommentView.as_view()),
    path('article/<int:article_id>/comments/<int:parent_id>/comments/create/',
         CommentCreateToCommentView.as_view()),
]
