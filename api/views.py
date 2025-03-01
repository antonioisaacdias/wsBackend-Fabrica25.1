from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
import requests
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def authors(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def author(request, author_id):
    if request.method == 'GET':
        author = Author.objects.get(id=author_id)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        author = Author.objects.get(id=author_id)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        author = Author.objects.get(id=author_id)
        if author is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def articles(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def article(request, article_id):
    if request.method == 'GET':
        article = Article.objects.get(id=article_id)
        if article is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        article = Article.objects.get(id=article_id)
        if article is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        article = Article.objects.get(id=article_id)
        if article is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def article_by_slug(request, slug):
    article = Article.objects.get(slug=slug)
    if article is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['GET'])
def nyt_tech_articles(request):
    if request.method == 'GET':
        url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
        params = {'api-key': settings.NYT_API_KEY}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            results = data['results'][:5]
            articles = []
            
            for result in results:
                article = {
                    'title': result['title'],
                    'subject': result['subsection'],
                    'abstract': result['abstract'],
                    'created_at': result['published_date'],
                    'image': result['multimedia'][0]['url'],
                    'url': result['url']
                }
                articles.append(article)
        
        else:
            articles = []    
        
        return Response(articles)