import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView

from backend.models import Book, Author, Movie
# from .forms import
from pages.forms import MovieForm


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


def movie_list_and_create(request):
    form = MovieForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = MovieForm()

    movie_list = Movie.objects.all()
    return render(request, 'pages/movie_list.html', {'list': movie_list, 'form': form})
