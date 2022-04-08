from django.urls import path
from .views import *


urlpatterns = [
    path('mypage/', user_page, name='user_page'),
    path('friends/', friends, name='friends'),
    path('settings/', settings, name='settings'),
    path('login/', login, name='login'),
]
