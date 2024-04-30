from django.db import models


class Professions(models.Model):
    title = models.CharField(max_length=255)
    faculty = models.TextField(verbose_name='Факультет')
    image_link = models.URLField(verbose_name='Ссылка на главное изображение')
    description = models.TextField(verbose_name='Описание профессии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Tag(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    name = models.TextField(verbose_name='Имя тэга')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tэг'
        verbose_name_plural = 'Тэги'


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
    image_link = models.TextField(verbose_name='Ссылка на иконку')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Bachelor(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    faculty_name = models.CharField(max_length=255, verbose_name='Название факультета')
    speciality_name = models.CharField(max_length=255, verbose_name='Название специальности')
    link = models.URLField(verbose_name='Ссылка на специальность')

    def __str__(self): 
        return self.speciality_name

    class Meta:
        verbose_name = 'Бакалавриат'
        verbose_name_plural = 'Бакалавриат'


class Master(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    faculty_name = models.CharField(max_length=255, verbose_name='Название факультета')
    speciality_name = models.CharField(max_length=255, verbose_name='Название специальности')
    link = models.URLField(verbose_name='Ссылка на специальность')

    def __str__(self): 
        return self.speciality_name

    class Meta:
        verbose_name = 'Магистратура'
        verbose_name_plural = 'Магистратура'


class FurtherEducation(models.Model):
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
    link = models.URLField(verbose_name='Ссылка на вакансию')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия HH'
        verbose_name_plural = 'Вакансии HH'


class Partners(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    name = models.CharField(max_length=255, verbose_name='Название партнера')
    link = models.URLField(verbose_name='Ссылка на партнера')
    image_link = models.URLField(verbose_name='Ссылка на изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
    

class UsefulLink(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE, verbose_name='Профессия')
    name = models.CharField(max_length=255, verbose_name='Название ссылки')
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Полезная ссылка'
        verbose_name_plural = 'Полезные ссылки'
