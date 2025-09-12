from rest_framework import serializers
from .models import Book, Author, Category
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author; fields = ['id','name','bio']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category; fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(write_only=True, source='author', queryset=Author.objects.all())
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, source='category', queryset=Category.objects.all())
    class Meta:
        model = Book
        fields = ['id','title','description','author','category','author_id','category_id','price','rating','published_date']
