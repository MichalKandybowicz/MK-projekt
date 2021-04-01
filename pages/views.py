from django.db.models.query_utils import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView, ListView

from backend.models import CustomUser, Book, Author


# from .forms import


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'pages/book_detail.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'pages/author_detail.html'


class BooksListPageView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'pages/books_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(BooksListPageView, self).get_context_data(**kwargs)
        return context