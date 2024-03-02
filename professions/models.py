from django.db import models

# Create your models here.
class Professions(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

class Promo(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    image = models.ImageField(upload_to='promo_images/', verbose_name='Фото промо')
    description = models.TextField(verbose_name='Описание профессии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Промо'
        verbose_name_plural = 'Промо'

class Task(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    title = models.CharField(max_length=255, verbose_name='Название Задачи')
    text = models.TextField(verbose_name='Текст задачи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Map(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')

    def __str__(self):
        return f"Карта для {self.profession}"

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

class MapPointer(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='pointers', verbose_name='Карта')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price_min = models.CharField(max_length=255, verbose_name='Минималная цена')
    price_max = models.CharField(max_length=255, verbose_name='Максимальная цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Метка на карте'
        verbose_name_plural = 'Метки на карте'

class Card(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    title = models.CharField(max_length=255, verbose_name='Название карточки')
    text = models.TextField(verbose_name='Текст карточки')
    image = models.ImageField(upload_to='card_images/', verbose_name='Фото карточки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

class Speciality(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    academic_degree = models.CharField(max_length=255, verbose_name='Академическая степень')
    name = models.CharField(max_length=255, verbose_name='Название специальности')
    faculty = models.CharField(max_length=255, verbose_name='Факультет')
    budget_places_count = models.IntegerField(verbose_name='Бюджетные места')
    year_budget_places_count = models.IntegerField(null=True, verbose_name='Год бюджетных мест')
    passing_score = models.IntegerField(verbose_name='Количество мест')
    year_passing_score = models.IntegerField(null=True, verbose_name='Год количества мест')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена обучения')
    year_price = models.IntegerField(null=True, verbose_name='Год цены обучения')
    period = models.IntegerField(verbose_name='Период обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Академическая степень'
        verbose_name_plural = 'Академические степени'