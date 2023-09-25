from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('rooms/', include('room.urls')),
    
    path('api/drf-auth/', include('rest_framework.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]