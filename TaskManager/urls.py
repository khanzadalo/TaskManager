from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('', include('users.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

