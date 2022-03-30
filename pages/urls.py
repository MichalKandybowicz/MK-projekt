from django.urls import path

from .views import HomePageView, AboutPageView, BooksListPageView, BookDetailView, AuthorDetailView, \
    FarmPageView, \
    books_to_csv, \
    movie_list_and_create

# MovieListWithForm, \


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('books/', BooksListPageView.as_view(), name='books_list'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail-view'),
    path('farm/', FarmPageView.as_view(), name='farm'),
    path('export/books-to-csv/', books_to_csv, name='books_to_csv'),
    path('movies', movie_list_and_create, name='movies_list'),

]
