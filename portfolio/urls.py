from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from dashboard import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('', include('me.urls')),

    path('api/', views.api_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
