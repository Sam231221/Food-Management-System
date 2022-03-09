from django.contrib import admin
from django.urls import path, include
from MPhoto.views import photo_add_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MFood.urls')),
    path('photo/', photo_add_view, name='photo-view'),
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)