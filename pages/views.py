import csv

from django.db.models.query_utils import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView, ListView

from backend.models import CustomUser, Book, Author


# from .forms import


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class FarmPageView(TemplateView):
    template_name = 'farmer/farmer.html'


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


def books_to_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            "id ", "title ", "author ", "date_of_publication ", "book type "
         ]
    )
    books_list = Book.objects.all().order_by("id")
    for book in books_list:
        writer.writerow(
            [
                book.id,
                book.title,
                book.author,
                book.date_of_publication,
                book.book_type,

             ]
        )
    return response