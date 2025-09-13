from rest_framework import routers
from django.urls import path, include
from .views import BookViewSet, AuthorViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
