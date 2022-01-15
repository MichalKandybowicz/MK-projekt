from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('api_auth/', include('rest_framework.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html')), ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
