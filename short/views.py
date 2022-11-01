from django.http import HttpResponse
from django.shortcuts import render, redirect

from short.models import Url
from short.utils import random_choice


def index(request):
    return render(request, 'short/index.html', {})


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        short_link = random_choice()
        new_link = Url(link=link, short_link=short_link)
        new_link.save()
        return HttpResponse(short_link)


def redirect_url(request, pk):
    url_details = Url.objects.get(short_link=pk)
    return redirect(url_details.link)
