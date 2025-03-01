from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('', views.index, name='index'),
    path('editorial/', views.editorial, name='editorial'),
    path('accounts/login/', views.signin),
    path('logout/', views.signout, name='signout'),
    path('editorial/article/<str:slug>/', views.edit_article, name='edit_article'),
    path('editorial/article/', views.new_article, name='new_article'),
    path('<str:slug>/', views.full_article, name='full_article')
]