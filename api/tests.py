# Create your tests here.


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from short.models import Url


class UrlsTests(APITestCase):
    def test_create_new_url(self):
        """
        Ensure we can create a new URL object.
        """
        url = reverse('api:urls-list')
        data = {
            "link": "https://stackoverflow.com/test",
            "end_time": "2023-12-08T11:52:40.912434"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Url.objects.count(), 1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
