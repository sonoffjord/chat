from django.urls import path

from .views import MassageView


urlpatterns = [
    path('massages/', MassageView.as_view())
]
