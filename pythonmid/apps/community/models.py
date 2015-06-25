# coding=utf-8
import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


def image_path(self, filename):
    path = "Sponsor/{0}/image/".format(str(self.id))
    ext = filename.split('.')[-1]
    my_filename = "{0}.{1}".format(str(uuid.uuid1()).replace('-', ''), ext)
    url = os.path.join(path, my_filename)
    return url


def user_image_path(self, filename):
    path = "Users/{0}/ImageProfile/".format(str(self.user.id))
    ext = filename.split('.')[-1]
    my_filename = "{0}.{1}".format(str(uuid.uuid1()).replace('-', ''), ext)
    url = os.path.join(path, my_filename)
    return url


@python_2_unicode_compatible
class Sponsor(models.Model):

    SPONSOR_LEVEL = (
        (1, 'Gold'),
        (2, 'Platinum'),
    )

    name = models.CharField(max_length=500)
    level = models.IntegerField(choices=SPONSOR_LEVEL, help_text="Nivel Prioridad Sponsor")
    about = models.TextField(max_length=500, null=True, blank=True)
    website = models.URLField(max_length=700, help_text="URL de sitio oficial")
    logo = models.ImageField(upload_to=image_path, help_text="imagen del patrocinador")
    provides = models.CharField(max_length=600, help_text="Recurso o actividad que aporta a la comunidad")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to=user_image_path, null=True, blank=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Perfiles de Usuario"
        verbose_name = "Perfil de usuario"