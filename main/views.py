from re import template
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Post

class BlogCreateView(CreateView): 
    model = Post
    template_name = 'post_write.html'
    fields = ['title', 'body']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'
    