# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pythonmid.apps.community.models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(default=1, help_text=b'imagen del patrocinador', upload_to=pythonmid.apps.community.models.image_path),
            preserve_default=False,
        ),
    ]
