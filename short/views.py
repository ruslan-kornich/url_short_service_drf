import datetime
from datetime import timedelta

from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status

from short.models import Url
from short.utils import random_choice
from .validator import is_valid_url
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request, 'short/index.html', {})

@login_required
def create(request):
    if request.method == 'POST':
        current_site = get_current_site(request).domain
        current_user = request.user
        print(current_user)
        link = request.POST['link']
        day = request.POST['rng']
        time_create = datetime.datetime.now()
        end_time = time_create + timedelta(days=int(day))
        if is_valid_url(link):
            if Url.objects.filter(link=link).exists():
                link_in_base = Url.objects.get(link=link)
                link_in_base.end_time = end_time
                link_in_base.save()
                if link_in_base is not None:
                    return HttpResponse(current_site + "/" + link_in_base.short_link, status=status.HTTP_200_OK)
            else:
                short_link = random_choice()
                new_link = Url(user=current_user, link=link, short_link=short_link, time_create=time_create, end_time=end_time)
                new_link.save()
                return HttpResponse(current_site + "/" + short_link, status=status.HTTP_200_OK)

    return HttpResponse("Enter Correct URL", status=status.HTTP_200_OK)

@login_required
def redirect_url(request, pk):
    try:
        url_details = Url.objects.get(short_link=pk)
        return redirect(url_details.link)
    except Url.DoesNotExist:
        raise Http404("No URL matches the given query.")
