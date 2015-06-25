# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pythonmid.apps.events.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0006_auto_20150623_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='i_will',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Si'), (2, 'Maybe')], default=2),
        ),
        migrations.AddField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(help_text='Organizadores del evento', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(help_text='Evento', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='receive_news',
            field=models.BooleanField(default=False, help_text='Activar si desea recibir noticias del evento'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, help_text='Fecha en que confirma su asistencia'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(help_text='Participante del evento', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='from_datetime',
            field=models.DateTimeField(help_text='Fecha y hora de inicio'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Evento publicado'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=500, help_text='Nombre del evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(help_text='Sede del evento', to='events.Place'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(help_text='Patrocinadores del evento', to='community.Sponsor'),
        ),
        migrations.AlterField(
            model_name='event',
            name='to_datetime',
            field=models.DateTimeField(help_text='Fecha y hora de finalización'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='about',
            field=models.TextField(max_length=1000, help_text='Acerca del participante'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='description',
            field=models.TextField(max_length=1000, help_text='Detalle de la participación'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='duration',
            field=models.DurationField(help_text='Duración de la participación'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(help_text='Evento', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='participant',
            field=models.ForeignKey(help_text='Persona responsable de esta participación', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='title',
            field=models.CharField(max_length=600, help_text='Título de la participación'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='type',
            field=models.IntegerField(choices=[(0, 'Charla'), (1, 'Charla relámpago'), (2, 'Taller')], help_text='Tipo de participación'),
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.TextField(max_length=1000, blank=True, null=True, help_text='Dirección del lugar'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, help_text='Foto del lugar', upload_to=pythonmid.apps.events.models.image_path_places),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.CharField(max_length=20, help_text='Latitude'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.CharField(max_length=20, help_text='Longitude'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=500, help_text='Nombre del lugar de encuentro'),
        ),
    ]
