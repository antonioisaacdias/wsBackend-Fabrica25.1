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
            url = settings.INTERNAL_API_URL + 'auth/login/'
            response = requests.post(url, data={'username': username, 'password': password})
            if response.status_code == 200:
                token = response.json()['token']
                request.session['token'] = token
                return redirect('editorial')
                
        return render(request, 'frontend/login.html', {'error': 'Usuário ou senha inválidos'})

    if request.method == 'GET':
        return render(request, 'frontend/login.html')


@login_required
def signout(request):
    token = request.session['token']
    
    if token:
        url = settings.INTERNAL_API_URL + 'auth/logout/'
        requests.get(url, headers={'Authorization': 'Token ' + token})
        
    logout(request)
    request.session.flush()
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

@login_required
def new_article(request):
    if request.method == 'GET':
        url = settings.INTERNAL_API_URL + 'authors/'
        response = requests.get(url)
        authors = response.json()
        return render(request, 'frontend/new_article.html', {'authors': authors})
    if request.method == 'POST':

        url = settings.INTERNAL_API_URL + 'articles/'
        data = {
            'title': request.POST.get('title'),
            'subject': request.POST.get('subject'),
            'resume': request.POST.get('resume'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author'),
        }
        token = request.session['token']
        print(data)
        
        if token:
            url = settings.INTERNAL_API_URL + 'articles/'
            request_headers = {'Authorization': 'Token ' + token}
            response = requests.post(url, data=data, headers=request_headers)
            if response.status_code == 201:
                return redirect('editorial')
            else:
                return redirect('editorial', {'error', 'Ocorreu um erro ao salvar o artigo.'})
        
        return redirect('index')
    
