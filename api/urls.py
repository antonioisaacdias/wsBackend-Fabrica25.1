from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.authors),
    path('authors/<uuid:author_id>/', views.author),
    path('articles/', views.articles),
    path('articles/<uuid:article_id>/', views.article),
    path('articles/<str:slug>/', views.article_by_slug),
    path('articles/nyt/tech/', views.nyt_tech_articles),
]