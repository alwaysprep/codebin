# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20150821_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(max_length=64, choices=[('Pyhton', 'Pyhton'), ('JavaScript', 'JavaScript'), ('Ruby', 'Ruby')], default='py'),
        ),
    ]
