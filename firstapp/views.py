from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    return render(request, 'firstapp/home.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)#ata ami onno aktaresource sheke shikechi
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'firstapp/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() #ami module onusare use korinai ata oono jaiga theke sikhci
            login(request, user)
            messages.success(request, 'Logged In Successfully')
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'firstapp/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'firstapp/profile.html')

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Password changed successfully!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'firstapp/change_password.html', {'form': form})