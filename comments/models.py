from django.db import models
from authors.models import Author
from gists.models import Gist
# Create your models here.


class Comment(models.Model):
    gist = models.ForeignKey(Gist)
    author = models.ForeignKey(Author)
    text = models.TextField()

    def __str__(self):
        return self.text
