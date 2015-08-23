# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_remove_snippet_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='slug',
            field=models.SlugField(max_length=255, default=''),
        ),
    ]
