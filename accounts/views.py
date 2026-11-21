from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.user.is_authenticated: return redirect('core:home')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'حساب کاربری شما ساخته شد.')
        return redirect('core:home')
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated: return redirect('core:home')
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('core:home')
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST': logout(request)
    return redirect('core:home')
