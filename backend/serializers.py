from rest_framework import serializers

from backend.models import Author, BookType, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name', 'date_of_birth', 'date_of_death', 'note']


class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = ['url', 'title']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'author', 'book_type', 'title', 'note', 'date_of_publication']
