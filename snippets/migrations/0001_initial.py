# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(max_length=2, choices=[('py', 'Pyhton'), ('js', 'JavaScript'), ('ra', 'Raw Text'), ('rb', 'Ruby')])),
                ('file_name', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True)),
                ('gist', models.ForeignKey(to='gists.Gist')),
            ],
        ),
    ]
