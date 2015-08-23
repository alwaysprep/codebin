from django.db import models
from django.utils.text import slugify
from authors.models import Author
# Create your models here.


class Gist(models.Model):
    TEMPLATES = (
        ("ambiance", "ambiance"),
        ("chaos", "chaos"),
        ("chrome", "chrome"),
        ("clouds", "clouds"),
        ("clouds_midnight", "clouds_midnight"),
        ("cobalt", "cobalt"),
        ("crimson_editor", "crimson_editor"),
        ("dawn", "dawn"),
        ("dreamweaver", "dreamweaver"),
        ("eclipse", "eclipse"),
        ("github", "github"),
        ("idle_fingers", "idle_fingers"),
        ("iplastic", "iplastic"),
        ("katzenmilch", "katzenmilch"),
        ("kr_theme", "kr_theme"),
        ("kuroir", "kuroir"),
        ("merbivore", "merbivore"),
        ("merbivore_soft", "merbivore_soft"),
        ("mono_industrial", "mono_industrial"),
        ("monokai", "monokai"),
        ("pastel_on_dark", "pastel_on_dark"),
        ("solarized_dark", "solarized_dark"),
        ("solarized_light", "solarized_light"),
        ("sqlserver", "sqlserver"),
        ("terminal", "terminal"),
        ("textmate", "textmate"),
        ("tomorrow", "tomorrow"),
        ("tomorrow_night", "tomorrow_night"),
        ("tomorrow_night_blue", "tomorrow_night_blue"),
        ("tomorrow_night_bright", "tomorrow_night_bright"),
        ("tomorrow_night_eighties", "tomorrow_night_eighties"),
        ("twilight", "twilight"),
        ("vibrant_ink", "vibrant_ink"),
        ("xcode", "xcode"),
    )

    theme = models.CharField(max_length=64, choices=TEMPLATES, default="monokai")

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    isPrivate = models.BooleanField(default=False)
    author = models.ForeignKey(Author)
    slug = models.SlugField(max_length=255, default="")

    class Meta:
        unique_together = (
            ("author", "title")
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Gist, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
