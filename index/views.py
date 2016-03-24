from django.contrib import auth
from django.shortcuts import render


def basic(request):
    return render(request, 'indexlogin.html', {'username': auth.get_user(request).username})

