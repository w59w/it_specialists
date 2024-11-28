
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ITSpecialist

class RegistrationForm(UserCreationForm):
    class Meta:
        model = ITSpecialist
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'qualification']

class LoginForm(AuthenticationForm):
    class Meta:
        model = ITSpecialist
        fields = ['username', 'password']
