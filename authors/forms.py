__author__ = 'oguzhansagoglu'
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("image",)


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")
