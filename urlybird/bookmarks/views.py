from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


def redirect_url(request):
    return HttpResponseRedirect("http://www.google.com")
