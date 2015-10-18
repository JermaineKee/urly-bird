from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate


# Create your views here.


def redirect_url(request):
    request_path = request.path
    return HttpResponseRedirect("http://www.google.com")


def create_short(request):
    print(dir(request))
    pass


def index(request):
    return render(request,
                  'bookmarks/index.html')


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        authenticate.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('accounts/invalid')
    return render(request, "bookmarks/index.html")


def logout_success(request):
    logout(request)
    return render(request, "bookmarks/index.html")


def loggedin(request):
    return render('loggedin.html' ('username', request.user.username))


def invalid_login(request):
    return render('invalid_login.html')


def logout(request):
    authenticate.logout(request)
    return render('logout.html')
