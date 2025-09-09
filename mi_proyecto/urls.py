from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),                  # Home principal (si existe core/urls.py)
    path('blog/', include('blog.urls')),             # Blog
    path('accounts/', include('accounts.urls')),     # Usuarios
    path('messages/', include('messenger.urls')),    # Mensajería
    path('mi_app1/', include('mi_app1.urls')),       # App de vinos

    path('accounts/login/',  auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

