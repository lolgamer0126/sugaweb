from django.urls import path
from .import views
urlpatterns = [
    path('newtreh/', views.post, name = 'newtreh'),
]
