from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response

from short.models import Url
from .serializers import ShortURLSerializer


class ShortUrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = ShortURLSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(f"Link {instance} removed", status=status.HTTP_200_OK)

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
