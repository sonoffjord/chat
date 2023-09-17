from django.urls import path
from django.contrib.auth import views as auth_views

from .views import frontpage, signup



urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/form.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
