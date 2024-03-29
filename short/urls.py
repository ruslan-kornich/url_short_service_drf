from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<str:pk>", views.redirect_url, name="redirect"),
    path("user_urls/", views.user_urls, name="user_urls"),
]
