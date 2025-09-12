from django.urls import path
from django.shortcuts import render
def books_view(request): return render(request, 'store/books.html')
urlpatterns = [path('', books_view, name='books')]
