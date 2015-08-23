# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20150822_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='file_name',
            field=models.CharField(max_length=255),
        ),
    ]
