import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "short_url.settings")

import django

django.setup()

import json
import pytest
from short.models import Url
from django.urls import reverse

link_url = reverse("api:urls-list")
pytestmark = pytest.mark.django_db


# -------------------Test Get URLs -------------------------
def test_zero_urls_should_return_empty_list(client) -> None:
    response = client.get(link_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_url_exists_should_succeed(client) -> None:
    test_link = Url.objects.create(link="https://docs.djangoproject.com/en/4.1/")
    response = client.get(link_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("link") == test_link.link
    assert response_content.get("short_link") == ""


# -------------------Test POST URLs -------------------------
def test_create_url_without_arguments_should_fail(client) -> None:
    response = client.post(path=link_url)
    assert response.status_code == 400
    assert json.loads(response.content) == ["Error"]


def test_create_existing_url_should_be_succeed(client) -> None:
    Url.objects.create(link="https://www.google.com/")
    response = client.post(
        path=link_url,
        data={
            "link": "https://www.google.com/",
            "end_time": "2024-01-21T14:24:13.773645",
        },
    )
    assert response.status_code == 201


def test_create_wrong_url_should_fail(client) -> None:
    response = client.post(path=link_url)
    assert response.status_code == 400
