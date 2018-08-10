from django.db import models

class Otdel(models.Model):
    name = models.CharField(max_length=100)
    # work = models.K
    class Meta:
        """Служит для перевода класса"""
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name