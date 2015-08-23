# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20150822_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='slug',
        ),
    ]
