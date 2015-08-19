from django.db import models
from gists.models import Gist

# Create your models here.


class Snippet(models.Model):
    LANGUAGES = (
        ("py", "Pyhton"),
        ("js", "JavaScript"),
        ("ra", "Raw Text"),
        ("rb", "Ruby")
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    file_name = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    gist = models.ForeignKey(Gist)

    def __str__(self):
        return self.file_name
