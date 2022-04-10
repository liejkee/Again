from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import *
from .models import *

menu = [{'title': 'My page', 'url_name': 'user_page'},
        {'title': 'My friends', 'url_name': 'friends'},
        {'title': 'Settings', 'url_name': 'settings'},
        {'title': 'Log out', 'url_name': 'login'}]


def user_page(request):
    app_elements = UserInfo.objects.all()
    return render(request, 'socialnet/user_page.html', {'app_elements': app_elements, 'menu': menu,
                                                        'title': 'My page'})


def friends(request):
    return render(request, 'socialnet/friends_page.html', {'menu': menu, 'title': 'My friends'})


def settings(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_page')
        else:
            form = UserForm()
    return render(request, 'socialnet/settings_page.html', {'form': form, 'menu': menu, 'title': 'Settings'})


def login(request):
    return render(request, 'socialnet/login_page.html', {'menu': menu, 'title': 'Login'})


def clean_first_name(self):
    first_name = self.clened_data['first_name']
    if len(first_name) > 5:
        raise ValidationError('Error')
    return first_name


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def view_404(request, exception=None):
    return redirect('user_page', permanent=False)
