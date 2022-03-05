from django.urls import path
from .views import BlogView, ArticleDetail

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
]
