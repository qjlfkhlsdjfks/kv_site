from django import forms
from space.models import ContactUs


class ContactUsForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Имя',
    }))
    last_name = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Фамилия',
    }))
    email = forms.CharField(max_length=100, error_messages={'required': 'Заполните это поле'}, widget=forms.EmailInput(attrs={
        'class': 'input-field',
        'placeholder': 'Имя',
    }))
    about = forms.CharField(error_messages={'required': 'Заполните это поле'}, widget=forms.Textarea(attrs={
        'class': 'textarea-field',
        'placeholder': 'О вас',
    }))
    comments = forms.CharField(error_messages={'required': 'Заполните это поле'}, widget=forms.Textarea(attrs={
        'class': 'textarea-field',
        'placeholder': 'Коментарий',
    }))
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'about', 'comments']