from django.db import models
from django.conf import settings
# Create your models here.


class Author(models.Model):


    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to="profiles", null=True, blank=True)

    def __str__(self):
        return self.user.username
