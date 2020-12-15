from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'account/signup.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        user_name = request.POST.get('username', '')
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        confirm_pass = request.POST.get('confirm_pass', '')

        user_check = User.objects.filter(username=user_name)
        if user_check:
            messages.error(request, "Username already taken")
            return redirect('/')

        if password == confirm_pass:
            user_obj = User.objects.create_user(first_name=name, password=password, email=email, username=user_name)
            user_obj.save()

    return redirect('/userpage')


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        user_password = request.POST.get('password', '')

        user = authenticate(username=user_name, password=user_password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in')
            return redirect('/userpage')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/')


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('/')