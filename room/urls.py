from rest_framework import routers
from django.urls import path, include

from .views import rooms, room, RoomView, MessageView

router = routers.DefaultRouter()
router.register('', RoomView, basename='room')


urlpatterns = [
    path('', rooms, name='rooms'),
    path('<slug:slug>/', room, name='room'),
    path('messages/', MessageView.as_view()),
    path('api/', include(router.urls)),
]
