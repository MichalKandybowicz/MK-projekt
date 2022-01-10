from django.urls import path, include

from .views import HomePageView, AboutPageView, TestPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('test/', TestPageView.as_view(), name='test'),
    # path('books/', BooksListPageView.as_view(), name='books_list'),
    # path('book/<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
    # path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail-view'),
    # path('farm/', FarmPageView.as_view(), name='farm'),
    # path('export/books-to-csv/', books_to_csv, name='books_to_csv'),
    # path('movies', MovieListWithForm.as_view(), name='movies_list'),


]
