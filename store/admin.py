from django.contrib import admin
from .models import Author, Category, Book
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','category','price','rating','published_date']
    search_fields = ['title','author__name']
    list_filter = ['category']
