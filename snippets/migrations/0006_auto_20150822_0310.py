# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20150821_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='slug',
            field=models.SlugField(max_length=255, default=''),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='file_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(max_length=64, default='py', choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Ruby', 'Ruby')]),
        ),
    ]
