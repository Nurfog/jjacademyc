from django.contrib import admin
from django.urls import path, include
from jjacademyc import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('', include('lms.urls')),
    path('', include('autenticacion.urls')),
    path('', include('cms.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
