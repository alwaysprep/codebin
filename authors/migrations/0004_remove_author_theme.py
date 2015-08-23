# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20150821_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='theme',
        ),
    ]
