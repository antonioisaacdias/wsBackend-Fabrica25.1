from rest_framework import serializers
from .models import Author, Article

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
        
class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'subject', 'resume', 'content', 'author_name', 'created_at', 'is_active']