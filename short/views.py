from django.http import HttpResponse
from django.shortcuts import render, redirect
from short.models import Url
from short.utils import random_choice
from .validators import validate_url
import datetime
from datetime import timedelta


def index(request):
    return render(request, 'short/index.html', {})


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        day = request.POST['rng']
        if validate_url(link):
            short_link = random_choice()
            time_create = datetime.datetime.now()
            end_time = time_create + timedelta(days=int(day))
            new_link = Url(link=link, short_link=short_link, time_create=time_create, end_time=end_time)
            new_link.save()
            return HttpResponse(short_link)


def redirect_url(request, pk):
    url_details = Url.objects.get(short_link=pk)
    return redirect(url_details.link)
