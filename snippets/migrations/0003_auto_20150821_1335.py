# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20150821_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('Pyhton', 'Pyhton'), ('JavaScript', 'JavaScript'), ('Ruby', 'Ruby')], max_length=2, default='py'),
        ),
    ]
