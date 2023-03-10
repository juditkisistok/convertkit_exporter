from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

class APIForm(UserChangeForm):
    password = None
    class Meta:
        model = Profile
        fields = ['ck_api', 'ck_secret']
        labels = {
            'ck_api': 'ConvertKit API key',
            'ck_secret': 'Convertkit API secret'
        }
        widgets = {
            'ck_secret': forms.PasswordInput
        }