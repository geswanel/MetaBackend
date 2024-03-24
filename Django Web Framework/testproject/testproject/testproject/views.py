from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


def handler404(request, exception):
    return HttpResponse(f"<h1>Page Not Found</h1><p><a href=\"{reverse('myapp:index')}\">Go to homepage</a></p>", status='404')