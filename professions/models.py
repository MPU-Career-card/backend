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
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='promo_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()

class Task(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()

class Map(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)

class MapPointer(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='pointers')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_min = models.CharField(max_length=255)
    price_max = models.CharField(max_length=255)

class Card(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='card_images/')

class Speciality(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)
    academic_degree = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    budget_places_count = models.IntegerField()
    year_budget_places_count = models.IntegerField(null=True)
    passing_score = models.IntegerField()
    year_passing_score = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year_price = models.IntegerField(null=True)
    period = models.IntegerField()