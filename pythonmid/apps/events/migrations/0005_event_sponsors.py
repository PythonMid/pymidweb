# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_userprofile'),
        ('events', '0004_auto_20150527_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ForeignKey(blank=True, to='community.Sponsor', null=True),
        ),
    ]
