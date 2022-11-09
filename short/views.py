import datetime
from datetime import timedelta

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

from short.models import Url
from short.utils import random_choice
from .validators import validate_url


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
    try:
        url_details = Url.objects.get(short_link=pk)
        return HttpResponseRedirect(url_details.link)
    except Url.DoesNotExist:
        raise Http404("No URL matches the given query.")

