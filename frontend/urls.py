from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('', views.index, name='index'),
    path('editorial/', views.editorial, name='editorial'),
    path('accounts/login/', views.signin),
    path('logout/', views.signout, name='signout'),
    path('editorial/article/<str:slug>/', views.article, name='article'),
]