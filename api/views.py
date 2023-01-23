from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from short.models import Url
from .serializers import ShortURLSerializer


class ShortUrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = ShortURLSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def list(self, request, **kwargs):
        queryset = Url.objects.all()
        serializer = ShortURLSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Url.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ShortURLSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:

            return Response(data={"Error"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(f"Link {instance} removed", status=status.HTTP_200_OK)

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
