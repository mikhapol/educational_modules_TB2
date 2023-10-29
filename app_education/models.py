from django.conf import settings
from django.db import models


# Create your models here.

class Education(models.Model):
    """Поля модели образовательных модулей"""

    serial = models.IntegerField(verbose_name='порядковый номер')
    title = models.CharField(verbose_name='название', max_length=50)
    desc = models.TextField(verbose_name='описание')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        managed = False
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'
