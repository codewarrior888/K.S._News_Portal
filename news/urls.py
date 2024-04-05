from django.urls import path
from .views import (
   NewsList, ArticlesList, PostDetail, PostSearch, NewsCreate, ArticleCreate, ArticleEdit,
   NewsEdit, ArticleDelete, NewsDelete, subscriptions,
                    )
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('news/', cache_page(60)(NewsList.as_view()), name='news_list'),
   path('articles/', ArticlesList.as_view(), name='articles_list'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<str:post_genre>/<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]
