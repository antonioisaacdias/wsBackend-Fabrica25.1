from django.shortcuts import render, redirect
import requests
from django.conf import settings
from .services import datetime_long_formater
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'frontend/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('editorial')
        
        return render(request, 'frontend/login.html', {'error': 'Usuário ou senha inválidos'})

    if request.method == 'GET':
        return render(request, 'frontend/login.html')


@login_required
def signout(request):
    logout(request)
    return redirect('index')

@login_required
def editorial(request):
    url = settings.INTERNAL_API_URL + 'articles/'
    response = requests.get(url)
    articles = response.json()
    
    for article in articles:
        article['created_at'] = datetime_long_formater(article['created_at'])
        
    return render(request, 'frontend/editorial.html', {'articles': articles})

def edit_article(request, slug):
    url = settings.INTERNAL_API_URL + 'articles/' + slug + '/'
    response = requests.get(url)
    article = response.json()
    article['created_at'] = datetime_long_formater(article['created_at'])
    
    return render(request, 'frontend/edit_article.html', {'article': article})

def new_article(request):
    return render(request, 'frontend/new_article.html')
