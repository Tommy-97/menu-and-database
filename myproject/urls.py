# myproject/urls.py

from django.urls import include, path

urlpatterns = [
    
    path('', include('menuapp.urls')),  
    
]
