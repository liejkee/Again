from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'My page', 'url_name': 'user_page'},
        {'title': 'My friends', 'url_name': 'friends'},
        {'title': 'Settings', 'url_name': 'settings'},
        {'title': 'Log out', 'url_name': 'login'}]


def user_page(request):
    app_elements = UserInfo.objects.all()
    return render(request, 'socialnet/user_page.html', {'app_elements': app_elements, 'menu': menu, 'title': 'My page'})


def friends(request):
    return render(request, 'socialnet/friends_page.html', {'menu': menu, 'title': 'My friends'})


def settings(request):
    return render(request, 'socialnet/settings_page.html', {'menu': menu, 'title': 'Settings'})


def login(request):
    return render(request, 'socialnet/login_page.html', {'menu': menu, 'title': 'Login'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def view_404(request, exception=None):
    return redirect('main_page', permanent=False)
