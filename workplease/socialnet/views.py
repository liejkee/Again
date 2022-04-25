from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

menu = [{'title': 'My page', 'url_name': 'user_page'},
        {'title': 'My friends', 'url_name': 'friends'},
        {'title': 'Settings', 'url_name': 'settings'},
        {'title': 'Test Items', 'url_name': 'test_items'},
        {'title': 'Logout', 'url_name': 'logout_user'}]


@login_required(login_url='login_user')
def user_page(request):
    app_elements = UserInfo.objects.all()[:1]
    return render(request, 'socialnet/user_page.html', {'app_elements': app_elements, 'menu': menu,
                                                        'title': 'My page'})


@login_required(login_url='login_user')
def edit_user_page(request):
    app_elements = UserInfo.objects.get(id=1)
    form = UserSettings(request.POST or None, instance=app_elements)
    if form.is_valid():
        messages.success(request, 'User data has changed successfully')
        form.save()
        return redirect('user_page')
    return render(request, 'socialnet/edit_user_page.html', {'menu': menu, 'app_elements': app_elements,
                                                             'title': 'Edit Information ', 'form': form})


@login_required(login_url='login_user')
def friends(request):
    return render(request, 'socialnet/friends_page.html', {'menu': menu, 'title': 'My friends'})


@login_required(login_url='login_user')
def settings(request):
    app_elements = UserInfo.objects.get(id=1)
    form = UserSettings()

    if request.method == 'POST':
        form = UserSettings(request.POST, instance=app_elements)
        if form.is_valid():
            messages.success(request, 'User data has changed successfully')
            form.save()
            return redirect('settings')

    return render(request, 'socialnet/settings_page.html', {'form': form, 'menu': menu,
                                                            'title': 'Settings'})


@login_required(login_url='login_user')
def test_items(request):
    return render(request, 'socialnet/test_items_page.html', {'menu': menu, 'title': 'Test Items',
                                                              'test_items': test_items})


def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_page')

    return render(request, 'socialnet/login_page.html', {'page': page})


def logout_user(request):
    logout(request)
    return redirect('login_user')


def register(request):
    page = 'register'
    form = UserForm(request.POST)

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('user_page')

    return render(request, 'socialnet/login_page.html', {'form': form, 'page': page})


def view_404(request, exception=None):
    return redirect('user_page', permanent=False)
