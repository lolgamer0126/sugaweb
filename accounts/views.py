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

def newtreh(request):

    if request.method == 'POST':

            if request.POST.get("submit")==("register"):
                    form = CustomUserCreationForm(request.POST)
                    if form.is_valid():
                            form.save()
                            username = form.cleaned_data.get('username')
                            email = form.cleaned_data.get('email')
                            raw_password = form.cleaned_data.get('password1')
                            user = CustomUser.objects.create_user(username = username, email = email,  password= raw_password)
                            user.save()
                            login(request, user)
                            return redirect('home')
            
            elif request.POST.get("submit")==("login"):  
                    form1 = AuthenticationForm(request, data=request.POST)
                    if form1.is_valid():
                        username = request.POST['email']
                        password = request.POST['password']
                        user = authenticate(email=username, password=password)
                        if user is not None:
                            login(request, user)
                            messages.info(request, f"You are now logged in as {username}.")
                            return redirect('home')
                    
                        else:
                            print("Neg ymchin buruu bn")
    else:
        form = CustomUserCreationForm
        form1 = AuthenticationForm
        return render(request, 'registration/sign.html')



def post(request):
    print(request.POST)

    if request.method == 'POST':
        print(request.POST['email'])

        if request.POST.get('submit') == 'register':

            user = CustomUser.objects.create_user(
                    username = request.POST["username"],
                    email=request.POST["email"], 
                    password = request.POST["password"]
                )
            user.save()
            return redirect('/')

        elif request.POST.get('submit') == 'login':

            email = request.POST['email']
            password = request.POST['password']
            username = CustomUser.objects.get(email=email.lower()).username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return render(request, 'registration/sign.html')


    else:
        return render(request, 'registration/sign.html')

def signup(request):
    if request.method == 'POST':
        user = CustomUser.objects.create_user(
                    username = request.POST["username"],
                    email=request.POST["email"], 
                    password = request.POST["password"]
                )
        user.save()

    else:
        return render(request, 'registration/login.html')


def view_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = CustomUser.objects.get(email=email.lower()).username

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'registration/in.html')

