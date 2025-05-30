from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django import forms

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    password2 = forms.CharField(
        label="Password Confirmation", widget=forms.PasswordInput, help_text=""
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class CustomPasswordChangeForm(PasswordChangeForm):
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput,
        help_text="",  # Removes the default message
    )
