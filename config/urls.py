from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from backend import views as b_views

api = routers.DefaultRouter()
api.register(r'attacks', b_views.AttackViewSet)

urlpatterns = [
                  path('accounts/', include('allauth.urls')),
                  path('', include('pages.urls')),
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('api/', include(api.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
