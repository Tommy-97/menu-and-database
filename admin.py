# admin.py
from django.contrib import admin

from menuapp.models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'order')
    list_filter = ('parent',)

admin.site.register(MenuItem, MenuItemAdmin)

