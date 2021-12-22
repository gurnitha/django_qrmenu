# qrmenu_backent/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
