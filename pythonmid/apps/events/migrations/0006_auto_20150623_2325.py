# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_userprofile'),
        ('events', '0005_event_sponsors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='sponsors',
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(help_text=b'Patrocinadores del evento', to='community.Sponsor'),
        ),
    ]
