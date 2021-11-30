from django.db import models
from django.shortcuts import resolve_url as r

from eventex.nucleo.managers import KindQuerySet
from eventex.nucleo.managers import PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    website = models.URLField('website', blank=True)
    photo = models.URLField('foto')
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone')
    )
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='palestrante')
    kind = models.CharField('Tipo', max_length=1, choices=KINDS)
    value = models.CharField('Valor', max_length=50)

    # Explicitando o modulo objects
    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value


class Activity(models.Model):
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)
    title = models.CharField('nome', max_length=200)
    start = models.TimeField('inicio', blank=True, null=True)
    description = models.TextField('descrição', blank=True)

    objects = PeriodManager()

    class Meta:
        abstract = True
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title


class Talk(Activity):
    pass


class Course(Activity):
    slots = models.IntegerField()

    objects = PeriodManager()

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return self.title
