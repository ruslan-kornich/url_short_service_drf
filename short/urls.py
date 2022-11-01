from django.urls import path
from datetime import timedelta

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.redirect_url, name='redirect'),
]
