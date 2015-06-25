# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pythonmid.apps.community.models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_sponsor_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='level',
            field=models.IntegerField(choices=[(1, 'Gold'), (2, 'Platinum')], help_text='Nivel Prioridad Sponsor'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(help_text='imagen del patrocinador', upload_to=pythonmid.apps.community.models.image_path),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='provides',
            field=models.CharField(max_length=600, help_text='Recurso o actividad que aporta a la comunidad'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='website',
            field=models.URLField(max_length=700, help_text='URL de sitio oficial'),
        ),
    ]
