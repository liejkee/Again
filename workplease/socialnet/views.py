from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

menu = [{'title': 'My page', 'url_name': 'user_page'},
        {'title': 'My friends', 'url_name': 'friends'},
        {'title': 'Settings', 'url_name': 'settings'},
        {'title': 'Log out', 'url_name': 'login'}]


def user_page(request):
    app_elements = UserInfo.objects.all()[:1]
    return render(request, 'socialnet/user_page.html', {'app_elements': app_elements, 'menu': menu,
                                                        'title': 'My page'})


def friends(request):
    return render(request, 'socialnet/friends_page.html', {'menu': menu, 'title': 'My friends'})


# def settings(request):
#     form = UserForm()
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('settings')
#     return render(request, 'socialnet/settings_page.html', {'form': form, 'menu': menu, 'title': 'Settings'})


def login(request):
    return render(request, 'socialnet/login_page.html', {'menu': menu, 'title': 'Login'})


def view_404(request, exception=None):
    return redirect('user_page', permanent=False)


def settings(request):
    app_elements = UserInfo.objects.get(id=1)
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, instance=app_elements)
        if form.is_valid():
            messages.success(request, 'User data has changed successfully')
            form.save()
            return redirect('settings')

    return render(request, 'socialnet/settings_page.html', {'form': form, 'menu': menu,
                                                            'title': 'Settings'})
