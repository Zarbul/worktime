from django.db import models
from django.utils import timezone
# Create your models here.


class Worker(models.Model):
    name = models.CharField('Имя', max_length = 100)
    fname = models.CharField('Фамилия', max_length = 100)
    status = models.IntegerField(choices=((0, 'new'), (1, 'work'), (2, 'deleled')))
    # status = models.IntegerField(choices=)
    create_date = models.DateTimeField('Дата создания', default = timezone.now)
    balance = models.FloatField('Баланс денег', default = 0)
    class Meta:
        """Служит для перевода класса Post"""
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'
    def __str__(self):
        return '{} {}'.format(self.name, self.fname)
    def __del__(self):
        pass

class Contact(models.Model):
    type_contact = models.IntegerField('Тип контакта (телефон / e-mail)', choices = ((0, 'phone'), (1, 'e-mail')))
    contact = models.CharField('Контакт', max_length=256)
    worker = models.ForeignKey('Worker')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return '{} {}'.format(self.worker, self.contact)


class Adress(models.Model):
    indx = models.IntegerField('Индекс', max_length=6)
    region = models.CharField('Регион проживания', max_length=50)
    sity = models.CharField('Город проживания', max_length=50)
    street = models.CharField('Улица', max_length=50)
    home = models.CharField('Дом', max_length=9999)
    flat = models.IntegerField('Квартира')
    worker = models.ForeignKey('Worker')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return 'Домашний адрес: {}, {}, {}, {}, {}, {}'.format(self.indx, self.region, self.sity, self.street, self.home,
                                                                 self.flat)
