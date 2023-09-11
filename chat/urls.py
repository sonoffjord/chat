from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from .views import MassageView, RoomView, frontpage, signup

# router = DefaultRouter()
# router.register('', RoomView)


urlpatterns = [
    path('messages/', MassageView.as_view(), name='messages'),
    path('rooms/', RoomView.as_view(), name='rooms'),
    # path('rooms/<int:pk>',),
    # path('rooms/', include(router.urls)),
    path('frontpage/', frontpage, name='frontpage'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/form.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
