from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Memories(models.Model):
    """Воспоминания"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Введите воспоминание')
    comment = models.TextField(max_length=255, null=True, blank=True, verbose_name='Введите комментарий')
    location = models.PointField(srid=4326, verbose_name='Местоположение')

    def __str__(self):
        return f"<Model: User: {self.author}, Comment: {self.comment}, location: {self.location}>"

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
