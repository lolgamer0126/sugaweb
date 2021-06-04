from enum import auto
from re import template
from django import contrib
import django
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('',include('main.urls')),
]
