from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from accounts.models import CustomUser


class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    note = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('author-detail-view', args=[str(self.id)])


class BookType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('book-type-detail-view', args=[str(self.id)])


class Book(models.Model):
    author = models.ForeignKey(Author, related_name="book_author", on_delete=models.PROTECT)
    book_type = models.ForeignKey(BookType, related_name="book_type", on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    note = models.CharField(max_length=1000)
    date_of_publication = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('book-detail-view', args=[str(self.id)])


class Movie(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    votes = models.IntegerField(default=0)
    date_of_publication = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('movie-detail-view', args=[str(self.id)])



