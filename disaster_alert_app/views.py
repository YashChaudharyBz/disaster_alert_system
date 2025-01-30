from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('../login')
    else:
        form = SignupForm()
    return render(request, 'disaster_alert_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../home')
    else:
        form = AuthenticationForm()
    return render(request, 'disaster_alert_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('../login')

def home_view(request):
    return render(request, 'disaster_alert_app/home.html')
