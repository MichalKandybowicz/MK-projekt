from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend import views as b_views

api_books = routers.DefaultRouter()
api_books.register(r'author', b_views.AuthorViewSet)
api_books.register(r'book_type', b_views.BookTypeViewSet)
api_books.register(r'book', b_views.BookViewSet)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('api-books/', include(api_books.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
