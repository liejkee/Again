from django import template
from socialnet.models import *

register = template.Library()


@register.simple_tag()
def get_userinfo():
    return UserInfo.objects.all()
