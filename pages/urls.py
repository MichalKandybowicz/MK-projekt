from django.urls import path

from .views import HomePageView, AboutPageView, BooksListPageView, BookDetailView
from django.conf import settings
from django.conf.urls.static import static
# from .views import TradeView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('books/', BooksListPageView.as_view(), name='books_list'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail-view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
