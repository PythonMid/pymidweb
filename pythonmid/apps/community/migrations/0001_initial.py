# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('about', models.TextField(max_length=500, null=True, blank=True)),
                ('website', models.URLField(help_text=b'URL de sitio oficial', max_length=700)),
                ('provides', models.CharField(help_text=b'Recurso o actividad que aporta a la comunidad', max_length=600)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Patrocinador',
                'verbose_name_plural': 'Patrocinadores',
            },
        ),
    ]
