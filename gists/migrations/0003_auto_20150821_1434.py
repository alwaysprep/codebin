# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gists', '0002_gist_theme'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gist',
            unique_together=set([('author', 'title')]),
        ),
    ]
