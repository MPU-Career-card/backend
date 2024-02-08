from django.db import models


class Speciality(models.Model):
    tab_id = models.CharField(max_length=10)
    tab_label = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Specialities'


class Content(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE,
                                   related_name='content')
    tags = models.JSONField()
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Content'


class Card(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE,
                                related_name='cards')
    title = models.CharField(max_length=255)
    card_text = models.TextField()
    image = models.ImageField(upload_to='images/card_images/')

    class Meta:
        verbose_name_plural = 'Cards'
