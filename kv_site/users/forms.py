from django import forms
from users.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Имя',
    }))
    last_name = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Фамилия',
    }))
    username = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Логин',
    }))
    email = forms.EmailField(max_length=200, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Почта'
    }))
    password1 = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.PasswordInput(attrs={
        'class': 'input-field',
        'placeholder': 'Пароль',
    }))
    password2 = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.PasswordInput(attrs={
        'class': 'input-field',
        'placeholder': 'Подтвердите пароль',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Логин',
    }))
    password = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.PasswordInput(attrs={
        'class': 'input-field',
        'placeholder': 'Пароль',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'readonly': True,
    }))
    last_name = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'readonly': True,
    }))
    username = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
    }))
    email = forms.EmailField(max_length=200, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'readonly': True,
    }))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'image-field',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image']

