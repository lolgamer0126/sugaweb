from django.urls import path
from .views import BlogCreateView, BlogDetailView, HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('write', BlogCreateView.as_view(), name = 'write'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'detail'),
    
]
