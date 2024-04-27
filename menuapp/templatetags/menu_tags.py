from django import template

from menuapp.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent=None).order_by('order')
    return {
        'menu_items': menu_items,
        'menu_name': menu_name,
    }

@register.simple_tag
def my_custom_tag():
    # Your custom tag logic here
    return "Ну наконец то!!!"
