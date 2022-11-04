from django.utils import timezone
from short.models import Url


def cleaner_data():
    now = timezone.now()
    urls = Url.objects.all()
    for i in range(0, len(urls)):
        date = urls[i].end_time
        if date <= now:
            urls[i].delete()
