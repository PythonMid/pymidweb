# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20150624_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='from_time',
            field=models.DateTimeField(help_text='Hora de inicio'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='to_time',
            field=models.DateTimeField(help_text='Hora finaliza'),
        ),
    ]
