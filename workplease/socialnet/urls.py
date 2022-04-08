from django.urls import path
from .views import *


urlpatterns = [
    path('', user_page, name='user_page'),
    path('friends/', friends),
    path('settings/', settings),
    path('login/', login),
]
