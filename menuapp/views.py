#views.py

from django.http import HttpResponse
from django.shortcuts import render


def my_view(request):
    # Your view logic here
    return HttpResponse("наконец то, о да!")


def index(request):
    
    context = {
        'key1': 'value1',
        'key2': 'value2',
        }
    
    return render(request, 'draw_menu.html', context)


def my_page_view(request):
    return render(request, 'my_page.html')

