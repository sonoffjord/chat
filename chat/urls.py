from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MassageView, RoomView

router = DefaultRouter()
router.register('', RoomView)


urlpatterns = [
    path('massages/', MassageView.as_view()),
    path('rooms/', include(router.urls)),
]
