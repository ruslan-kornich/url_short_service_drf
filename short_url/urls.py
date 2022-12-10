from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

API_TITLE = "Short URL Service API "
API_DESCRIPTION = "Short URL Service API"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('short.urls')),
    path('api/v1/', include('api.urls', namespace='api')),
    path("api/v1/docs/", include_docs_urls(title=API_TITLE,
                                           description=API_DESCRIPTION)),
]
