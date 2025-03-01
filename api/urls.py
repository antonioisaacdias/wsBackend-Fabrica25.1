from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('authors/<uuid:author_id>/', views.author, name='author-detail'),
]