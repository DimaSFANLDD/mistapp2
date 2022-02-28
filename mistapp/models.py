from django.db import models


class Sorev(models.Model):
    name = models.CharField('Названия', max_length=150, blank=False, default='')
    descriptions = models.TextField('Описание', max_length=3000, blank=False, default='')
    members = models.CharField('Участники', max_length=150, blank=False, default='')
    result = models.CharField('Результаты', max_length=150, blank=False, default='')
