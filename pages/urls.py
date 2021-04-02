from django.urls import path, include

from .views import HomePageView, AboutPageView, BooksListPageView, BookDetailView, AuthorDetailView, FarmPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('books/', BooksListPageView.as_view(), name='books_list'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail-view'),
    path('farm/', FarmPageView.as_view(), name='farm'),
]
