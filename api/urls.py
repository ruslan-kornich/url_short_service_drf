from rest_framework import routers

from .views import ShortUrlViewSet

app_name = 'api'
routes = routers.SimpleRouter()
routes.register('urls', ShortUrlViewSet, basename='urls')
urlpatterns = [
    *routes.urls,
]
