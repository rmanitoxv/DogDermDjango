from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/', include('apps.user.urls')),
    path('api/', include('apps.clinics.urls')),
    path('api/', include('apps.diseases.urls')),
    path('api/', include('apps.results.urls')),
]
