from django.urls import path

from .views import MassageView, RoomView


urlpatterns = [
    path('massages/', MassageView.as_view()),
    path('rooms/', RoomView.as_view()),
]
