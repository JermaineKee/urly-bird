from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


def redirect_url(request):
    request_path = request.path
    return HttpResponseRedirect("http://www.google.com")


def create_short(request):
    print(dir(request))
    pass
