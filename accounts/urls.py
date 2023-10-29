from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    # добавьте другие маршруты, если это необходимо
]
