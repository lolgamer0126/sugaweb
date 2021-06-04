from re import template
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'