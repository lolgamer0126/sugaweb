from django import views
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.base import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.template import loader
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
User = get_user_model
def post(request):
    print(request.POST)
    if request.method == 'POST':

        if request.POST.get('submit') == 'register':

            #password check
            password = request.POST['password']
            password1 = request.POST['password1']
            email = request.POST['email']
            name = request.POST["username"]
            if CustomUser.objects.filter(email=email).exists():
                return HttpResponse('email already taken!')

            if CustomUser.objects.filter(username = name).exists():
                return HttpResponse('username already taken!')
            else:
                if password != password1:
                    return render(request, 'registration/sign.html', {"error': 'Password isn't same"})
                if len(password) < 8:
                    return render(request, 'registration/sign.html', {'error': "Bagadaa 8n orontoi baina"})
                user = CustomUser.objects.create_user(
                        username = request.POST["username"],
                        email=request.POST["email"], 
                        password = request.POST["password"]
                    )
                user.save()
                #auto login

                username = CustomUser.objects.get(email=email.lower()).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('home')

        elif request.POST.get('submit') == 'login':

            email = request.POST['email']
            password = request.POST['password']
            username = CustomUser.objects.get(email=email.lower()).username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')

    else:
        return render(request, 'registration/sign.html')



