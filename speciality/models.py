from django.db import models


class Speciality(models.Model):
    tab_id = models.CharField(max_length=10)
    tab_label = models.CharField(max_length=255)

    def __str__(self):
        return self.tab_id

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Content(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE,
                                   related_name='content')
    tags = models.JSONField()
    text = models.TextField()

    def __str__(self):
        return self.speciality
    
    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
    


class Card(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE,
                                related_name='cards')
    title = models.CharField(max_length=255)
    card_text = models.TextField()
    image = models.ImageField(upload_to='images/card_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
