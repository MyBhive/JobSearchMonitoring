from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignInForm(UserCreationForm):
    """Create form for sign_in"""
    surname = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    date_of_birth = forms.DateField()

    class Meta:
        model = CustomUser
        fields = [
            'surname',
            'name',
            'email',
            'password1',
            'password2',
            'date_of_birth'
        ]
