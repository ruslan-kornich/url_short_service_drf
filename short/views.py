from django.shortcuts import render


def index(request):
    return render(request, 'short/index.html', {})


def create(request):
    pass
