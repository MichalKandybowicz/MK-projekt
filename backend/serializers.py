from accounts.models import CustomUser
from rest_framework import serializers
from django.db.models.query_utils import Q

from backend.models import Author, BookType, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name', 'date_of_birth', 'date_of_death', 'photo', 'note']


class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = ['url', 'title']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'author', 'book_type', 'title', 'photo', 'note', 'date_of_publication']