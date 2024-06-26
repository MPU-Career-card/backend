from django.db import models


class Speciality(models.Model):
    faculty = models.TextField(verbose_name='Факультет')
    color = models.CharField(max_length=6, verbose_name='Цвет тикера (HEX)')
    code = models.CharField(max_length=255, verbose_name='Код направления')
    name = models.TextField(verbose_name='Название направления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
    

class Profession(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='Специальность')
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
