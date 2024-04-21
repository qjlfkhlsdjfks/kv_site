from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import logout
from users.forms import LoginForm, RegistrationForm, ProfileForm


def login(request):
    login_failed_message = ''
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('space:index'))
        else:
            login_failed_message = 'Ошибка! Неверный логин или пароль'
    else:
        form = LoginForm()
        
    context = {
        'title': 'Вход',
        'form': form,
        'login_failed_message': login_failed_message,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    registration_failed_message = ''
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            registration_failed_message = 'Ошибка! Проверьте правильность вводимых данных'
    else:
        form = RegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form,
        'registration_failed_message': registration_failed_message,
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Ваш Профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)


def logout_view(request):
    logout(request)
    
    return redirect(reverse('space:index'))

