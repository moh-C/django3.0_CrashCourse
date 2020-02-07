from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('django_starter.urls')),
]
