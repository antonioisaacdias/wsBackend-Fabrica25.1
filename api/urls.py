from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('authors/<uuid:author_id>/', views.author, name='author-detail'),
    path('articles/', views.articles, name='articles'),
    path('articles/<uuid:article_id>/', views.article, name='article-detail'),
    path('articles/<str:slug>/', views.article_by_slug, name='article-by-slug'),
    path('articles/nyt/tech/', views.nyt_tech_articles, name='nyt-tech-articles'),
]