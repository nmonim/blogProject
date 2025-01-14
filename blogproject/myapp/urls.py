from django.urls import path
from . import views
from .views import CommentListCreateAPIView, BlogList  # method 1
from .views import blog_comments # method 2

urlpatterns = [
    path('', BlogList.as_view(), name='blog_posts'),
    path('new/', BlogList.blog_create, name='blog_create'),
    # path('edit/<int:pk>/', BlogList.blog_update.as_view(), name='blog_update'),
    # path('delete/<int:pk>/', BlogList.blog_delete.as_view(), name='blog_delete'),
    path('api/blog/<int:pk>/comments', CommentListCreateAPIView.as_view(), name='blog_comments_api'),
    path('blog/<int:blog_id>/comments_test/', blog_comments, name='blog_comments_test'),
]