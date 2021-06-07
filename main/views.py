from re import template
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView, ListView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Post