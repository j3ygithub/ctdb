from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .static import static

urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('diary.urls')),
    path('', include('reminder.urls')),
    path('', include('telecom.urls')),
    path('', include('archive.urls')),
    path('log/', include('log.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

if settings.DEBUG or settings.USE_WHITENOISE:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
