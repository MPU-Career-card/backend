from django.db import models

# Create your models here.
class Professions(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

class Tag(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    name = models.TextField(verbose_name='Имя тэга')

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


class MapPointer(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    salary = models.CharField(max_length=255, verbose_name='Зарплата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Метка на карте'
        verbose_name_plural = 'Метки на карте'


class Skill(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    name = models.CharField(max_length=255, verbose_name='Название навыка')
    description = models.TextField(verbose_name='Описание навыка')
    svg = models.TextField(verbose_name='SVG иконка')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

class Bakalavr(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    faculty_name = models.CharField(max_length=255, verbose_name='Название факультета')
    speciality_name = models.CharField(max_length=255, verbose_name='Название специальности')
    link = models.URLField(verbose_name='Ссылка на специальность')

    def __str__(self): 
        return self.speciality_name
    class Meta:
        verbose_name = 'Бакалавриат'
        verbose_name_plural = 'Бакалавриат'
class Magistr(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    faculty_name = models.CharField(max_length=255, verbose_name='Название факультета')
    speciality_name = models.CharField(max_length=255, verbose_name='Название специальности')
    link = models.URLField(verbose_name='Ссылка на специальность')

    def __str__(self): 
        return self.speciality_name
    class Meta:
        verbose_name = 'Магистратура'
        verbose_name_plural = 'Магистратура'

class DPO(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    faculty_name = models.CharField(max_length=255, verbose_name='Название факультета')
    speciality_name = models.CharField(max_length=255, verbose_name='Название специальности')
    link = models.URLField(verbose_name='Ссылка на специальность')

    def __str__(self): 
        return self.speciality_name
    class Meta:
        verbose_name = 'ДПО'
        verbose_name_plural = 'ДПО'


class HHVacancy(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    link = models.CharField(max_length=255,verbose_name='Ссылка на вакансию')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия HH'
        verbose_name_plural = 'Вакансии HH'
class Partners(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    name = models.CharField(max_length=255, verbose_name='Название партнера')
    link = models.URLField(verbose_name='Ссылка на партнера')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
    
class UsefulLink(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    name = models.CharField(max_length=255, verbose_name='Название ссылки')
    link = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Полезная ссылка'
        verbose_name_plural = 'Полезные ссылки'
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