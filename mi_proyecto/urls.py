from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),                  # Home principal
    path('blog/', include('blog.urls')),             # Blog
    path('accounts/', include('accounts.urls')),     # Usuarios
    path('messages/', include('messenger.urls')),    # Mensajería
    path('mi_app1/', include('mi_app1.urls')),       # App de vinos
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)