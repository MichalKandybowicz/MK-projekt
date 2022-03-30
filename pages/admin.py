from django.contrib import admin

from backend.models import Author, BookType, Book, Movie

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(Movie)
