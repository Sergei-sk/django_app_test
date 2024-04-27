from menu.models import MenuPoint
from django import template
from django.shortcuts import redirect, render, get_object_or_404

register = template.Library()
arr = []


@register.inclusion_tag('menu/menu.html')
def show_menu(item):
    point = item.children.all()
    print('deti', item)
    print('point', point)
    return {
        "point": point,
    }

    