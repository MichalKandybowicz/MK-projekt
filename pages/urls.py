from django.urls import path, include

from .views import HomePageView, AboutPageView, test_page_view, register_request, login_request

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('test/', test_page_view, name='test'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
]


# path('books/', BooksListPageView.as_view(), name='books_list'),
# path('book/<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
# path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail-view'),
# path('farm/', FarmPageView.as_view(), name='farm'),
# path('export/books-to-csv/', books_to_csv, name='books_to_csv'),
# path('movies', MovieListWithForm.as_view(), name='movies_list'),
