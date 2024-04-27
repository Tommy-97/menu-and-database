#menuapp/urls.py

from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from . import views
from .views import my_page_view, my_view

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('my-page/', my_page_view, name='my_page'),
    path('', TemplateView.as_view(template_name='draw_menu.html'), name='index'),
    path('my-url/', my_view, name='my_view'),

]


