from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('urls/', views.UrlListView.as_view(), name='url_list'),
    path('urls/<str:short_link>/', views.UrlDetailView.as_view(), name='url_detail'),
]
