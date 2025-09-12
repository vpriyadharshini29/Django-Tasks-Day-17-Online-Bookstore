from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self): return self.name

class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    rating = models.FloatField(default=0)
    published_date = models.DateField(null=True, blank=True)
    def __str__(self): return self.title
