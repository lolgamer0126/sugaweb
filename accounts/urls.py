from django.urls import path
from .import views
urlpatterns = [
    path('sign/', views.post, name = 'sign'),
    path('burtguuleh/', views.signup, name = 'burguuleh'),
    path('newtreh/', views.view_login, name = 'newtreh'),
]
