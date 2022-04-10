from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name']
