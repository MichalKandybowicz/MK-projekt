from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend import views as b_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
