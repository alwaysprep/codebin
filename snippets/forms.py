from snippets.models import Snippet

__author__ = 'oguzhansagoglu'
from django import forms


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ("language", "file_name", "text")
