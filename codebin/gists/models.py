from django.db import models
from authors.models import Author
# Create your models here.


class Gist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    isPrivate = models.BooleanField(default=False)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title
