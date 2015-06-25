# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import pythonmid.apps.events.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(help_text=b'Fecha en que confirma su asistencia', auto_now_add=True)),
                ('receive_news', models.BooleanField(default=False, help_text=b'Activar si desea recibir noticias del evento')),
            ],
            options={
                'verbose_name': 'Participante de un evento',
                'verbose_name_plural': 'Participantes del evento',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Nombre del evento', max_length=500)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('about', models.TextField(help_text=b'Acerca del participante', max_length=1000)),
                ('image', models.ImageField(null=True, upload_to=pythonmid.apps.events.models.image_path_participant, blank=True)),
            ],
            options={
                'verbose_name': 'Participante',
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(help_text=b'Tipo de participaci\xc3\xb3n', choices=[(0, b'Charla'), (1, b'Charla rel\xc3\xa1mpago'), (2, b'Taller')])),
                ('title', models.CharField(help_text=b'T\xc3\xadtulo de la participaci\xc3\xb3n', max_length=600)),
                ('description', models.TextField(help_text=b'Detalle de la participaci\xc3\xb3n', max_length=1000)),
                ('duration', models.DurationField(help_text=b'Duraci\xc3\xb3n de la participaci\xc3\xb3n')),
                ('event', models.ForeignKey(help_text=b'Evento', to='events.Event')),
                ('participant', models.ForeignKey(help_text=b'Persona responsable de esta participaci\xc3\xb3n', to='events.Participant')),
            ],
            options={
                'verbose_name': 'Participaci\xf3n',
                'verbose_name_plural': 'Participaciones de un evento',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Nombre del lugar de encuentro', max_length=500)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('address', models.TextField(help_text=b'Direcci\xc3\xb3n del lugar', max_length=1000, null=True, blank=True)),
                ('latitude', models.CharField(help_text=b'Latitude', max_length=20)),
                ('longitude', models.CharField(help_text=b'Longitude', max_length=20)),
                ('image', models.ImageField(help_text=b'Foto del lugar', null=True, upload_to=pythonmid.apps.events.models.image_path_places, blank=True)),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(help_text=b'Sede del evento', to='events.Place'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(help_text=b'Evento', to='events.Event'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(help_text=b'Participante del evento', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='attendee',
            unique_together=set([('user', 'event')]),
        ),
    ]
