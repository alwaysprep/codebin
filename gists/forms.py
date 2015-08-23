from .models import Gist

__author__ = 'oguzhansagoglu'
from django import forms


class GistForm(forms.ModelForm):

    class Meta:
        model = Gist
        fields = ("title", "description", "isPrivate", "theme")

