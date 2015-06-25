# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150527_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(default=False, help_text=b'Evento publicado'),
        ),
    ]
