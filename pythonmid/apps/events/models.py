# coding=utf-8
import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from pythonmid.apps.community.models import Sponsor


def image_path_places(self, filename):
    path = "Places/{0}/image/".format(str(self.id))
    ext = filename.split('.')[-1]
    my_filename = "{0}.{1}".format(str(uuid.uuid1()).replace('-', ''), ext)
    url = os.path.join(path, my_filename)
    return url


def image_path_participant(self, filename):
    path = "Participant/{0}/image/".format(str(self.id))
    ext = filename.split('.')[-1]
    my_filename = "{0}.{1}".format(str(uuid.uuid1()).replace('-', ''), ext)
    url = os.path.join(path, my_filename)
    return url

@python_2_unicode_compatible
class Place(models.Model):
    name = models.CharField(max_length=500, help_text="Nombre del lugar de encuentro")
    description = models.TextField(max_length=1000, null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True, help_text="Dirección del lugar")
    latitude = models.CharField(max_length=20, help_text="Latitude")
    longitude = models.CharField(max_length=20, help_text="Longitude")
    image = models.ImageField(upload_to=image_path_places, null=True, blank=True, help_text="Foto del lugar")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

@python_2_unicode_compatible
class Event(models.Model):
    name = models.CharField(max_length=500, help_text="Nombre del evento")
    description = models.TextField(max_length=1000, null=True, blank=True)
    organizers = models.ManyToManyField(User, help_text="Organizadores del evento")
    sponsors = models.ManyToManyField(Sponsor, help_text="Patrocinadores del evento")
    from_datetime = models.DateTimeField(help_text="Fecha y hora de inicio")
    to_datetime = models.DateTimeField(help_text="Fecha y hora de finalización")
    place = models.ForeignKey(Place, help_text="Sede del evento")
    is_published = models.BooleanField(default=False, help_text="Evento publicado")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    @property
    def num_participants(self):
        """
        Retorna el número de participantes de un evento
        :return: Int
        """
        try:
            return Participant.objects.all().count()
        except:
            return 0
    
    @property
    def num_attendees(self):
        """
        Retorna el número de asistentes del evento
        """
        try:
            return Attendee.objects.filter(event=self).count()
        except:
            return 0

@python_2_unicode_compatible
class Attendee(models.Model):

    I_WILL = (
        (0, 'No'),
        (1, 'Si'),
        (2, 'Maybe'),
    )

    user = models.ForeignKey(User, help_text="Participante del evento")
    event = models.ForeignKey(Event, help_text="Evento")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Fecha en que confirma su asistencia")
    i_will = models.IntegerField(choices=I_WILL, default=2)
    receive_news = models.BooleanField(default=False, help_text="Activar si desea recibir noticias del evento")

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'event')
        verbose_name = "Asistentes"
        verbose_name_plural = "Asistentes"


class Participant(models.Model):

    name = models.CharField(max_length=500)
    about = models.TextField(max_length=1000, help_text="Acerca del participante")
    image = models.ImageField(upload_to=image_path_participant, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Participante"


class Participation(models.Model):
    PARTICIPATION_TYPE = (
        (0, 'Charla'),
        (1, 'Charla relámpago'),
        (2, 'Taller')
    )
    event = models.ForeignKey(Event, help_text="Evento")
    participant = models.ForeignKey(Participant, help_text="Persona responsable de esta participación")
    type = models.IntegerField(choices=PARTICIPATION_TYPE, help_text="Tipo de participación")
    title = models.CharField(max_length=600, help_text="Título de la participación")
    description = models.TextField(max_length=1000, help_text="Detalle de la participación")
    from_time = models.DateTimeField(help_text="Hora de inicio")
    to_time = models.DateTimeField(help_text="Hora finaliza")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Participación"
        verbose_name_plural = "Participaciones de un evento"