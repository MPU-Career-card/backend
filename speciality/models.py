from django.db import models


class Speciality(models.Model):
    tab_id = models.CharField(max_length=10, verbose_name='Номер академической степени')
    tab_label = models.CharField(max_length=255, verbose_name='Название академической степени')

    def __str__(self):
        return self.tab_id

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Content(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE,
                                   related_name='content')
    tags = models.CharField(max_length=255, verbose_name='Размер и цвет тега')
    text = models.TextField(verbose_name='Название специальности')

    def __str__(self):
        return self.speciality
    
    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
    


class Card(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE,
                                related_name='cards')
    title = models.CharField(max_length=255, verbose_name='Название Карточки')
    card_text = models.TextField(verbose_name='Описание карточки')
    image = models.ImageField(upload_to='images/card_images/', verbose_name='Изображение для карточки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
