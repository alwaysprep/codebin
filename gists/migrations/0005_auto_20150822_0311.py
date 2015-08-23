# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gists', '0004_auto_20150822_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gist',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
