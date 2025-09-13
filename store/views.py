from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author, Category
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author','category').all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = {
        'category__name':['exact'],
        'price':['gte','lte'],
        'author__name':['icontains'],
    }
    search_fields = ['title','author__name']
    ordering_fields = ['rating','published_date']
    ordering = ['-rating']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all(); serializer_class = AuthorSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all(); serializer_class = CategorySerializer
