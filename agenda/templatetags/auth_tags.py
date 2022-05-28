from multiprocessing.dummy import active_children
from django import template
from django.contrib.auth.models import Group

from users.models import Lid

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter(name="is_active")
def is_active(lid):
    return True if lid in Lid.objects.filter(active=True) else False
