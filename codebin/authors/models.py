from django.db import models
from django.conf import settings
# Create your models here.


class Author(models.Model):
    TEMPLATES = (
        ("D", "Dracula"),
        ("F", "Full Dark"),
        ("A", "Asphalt")
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    theme = models.CharField(max_length=1, choices=TEMPLATES)
    image = models.ImageField(null=True)

