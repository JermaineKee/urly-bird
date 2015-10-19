from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ShortForm
from .models import Click, Short

from hashids import Hashids


# Create your views here.


def redirect_url(request):
    request_path = request.path[1:]
    short_obj = Short.objects.get(short_url=request_path)
    click = Click(short_id=short_obj.id, timestamp=datetime.now())
    click.save()
    short_obj.click_count += 1
    short_obj.save()
    return HttpResponseRedirect(short_obj.bookmark)


def create_short(request):
    hashids = Hashids(salt='tiyd python 2015-08', alphabet='abcdefghijklmnopqrstuvwxyz0123456789')
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
            short.click_count = 0
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
