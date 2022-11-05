from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from short.models import Url
from .serializers import ShortURLSerializer


class ShortUrlView(APIView):

    def get(self, request):
        url = Url.objects.all()
        context = {
            "short_url": url.values(),
        }
        return Response(context)

    def post(self, request):
        link = request.data.get('short_url')
        serializer = ShortURLSerializer(data=link, many=True)
        if serializer.is_valid(raise_exception=True):
            url_save = serializer.save()
            context = {
                "success": f'Url {url_save[0]} created successfully'
            }
            return Response(context)

    def put(self, request):
        data = request.data.get('short_url')
        short = data[0]['short_link']
        saved_url = get_object_or_404(Url.objects.all(), short_link=short)
        serializer = ShortURLSerializer(instance=saved_url, data=data[0], partial=True)
        if serializer.is_valid(raise_exception=True):
            url_saved = serializer.save()
        return Response({
            "success": f"Url '{url_saved}' updated successfully",
        })

    def delete(self, request, format=None):
        data = request.data.get('short_url')
        short_link = data[0]['short_link']
        saved_url = get_object_or_404(Url.objects.all(), short_link=short_link)
        context = {
            "success": f'Url {saved_url.link} delete',
        }
        saved_url.delete()
        return Response(context)
