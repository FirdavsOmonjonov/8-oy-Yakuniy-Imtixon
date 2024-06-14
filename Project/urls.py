"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from Project import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Online Course API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Swagger schema'sini JSON formatida olish uchun URL
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # Swagger UI interfeysini olish uchun URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Redoc UI interfeysini olish uchun URL
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Django admin paneli uchun URL
    path('admin/', admin.site.urls),
    # DRF autentifikatsiyasi uchun URL (login/logout)
    path('api-auth/', include('rest_framework.urls')),
    # Kurs ilovasining barcha URLlari uchun asosiy namespace
    path('api/v1/', include('course.urls')),
    # Profil bo'limi uchun URL
    path('accounts/profile/', include('course.urls')),
    # Djoser autentifikatsiyasi uchun URL (oddiy)
    path('djoser-auth/', include('djoser.urls')),
    # Djoser token autentifikatsiyasi uchun URL
    path('auth/', include('djoser.urls.authtoken')),
    
]


if settings.DEBUG:
    # Media fayllarni xizmat qilish uchun URL konfiguratsiyasi
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)