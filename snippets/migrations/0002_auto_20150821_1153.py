# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='gist',
            field=models.ForeignKey(to='gists.Gist', related_name='snippets'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('py', 'Pyhton'), ('js', 'JavaScript'), ('ra', 'Raw Text'), ('rb', 'Ruby')], max_length=2, default='py'),
        ),
    ]
