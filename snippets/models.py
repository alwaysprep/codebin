from django.db import models
from django.utils.text import slugify
from gists.models import Gist

# Create your models here.


class Snippet(models.Model):
    LANGUAGES = (
        ("Python", "Python"),
        ("JavaScript", "JavaScript"),
        ("Ruby", "Ruby")
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=64, choices=LANGUAGES, default="py")
    file_name = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    gist = models.ForeignKey(Gist, related_name='snippets')
    slug = models.SlugField(max_length=255, default="")

    class Meta:
        unique_together = (
            ("file_name", "gist")
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.file_name)

        super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
        return self.file_name
