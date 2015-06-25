# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150624_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participation',
            name='duration',
        ),
        migrations.AddField(
            model_name='participation',
            name='from_time',
            field=models.TimeField(help_text='Hora de inicio', default=datetime.datetime(2015, 6, 25, 3, 35, 44, 747119, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participation',
            name='to_time',
            field=models.TimeField(help_text='Hora finaliza', default=datetime.datetime(2015, 6, 25, 3, 35, 54, 168409, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
