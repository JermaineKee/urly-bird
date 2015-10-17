from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ShortForm
from .models import Short

from hashids import Hashids


# Create your views here.


def redirect_url(request):
    request_path = request.path
    return HttpResponseRedirect("http://www.google.com")


def create_short(request):
    hashids = Hashids(salt='tiyd python 2015-08')
    short_hash = hashids.encode(Short.objects.last().id)
    if request.method == 'POST':
        form = ShortForm(request.POST)
        if form.is_valid():
            short = form.save(commit=False)
            print(type(request.user))
            if request.user.id is not None:
                short.user = request.user
            short.short_url = short_hash
            short.timestamp = datetime.now()
            short.save()

            return render(request,
                          'bookmarks/short.html',
                          {'short': short_hash})
    else:
        form = ShortForm()

    return render(request, 'bookmarks/index.html', {'form': form})


def index(request):
    return render(request,
                  'bookmarks/index.html')
