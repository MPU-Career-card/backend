from django.contrib import admin
from .models import Speciality, Content, Card

class SpecialityAdmin(admin.ModelAdmin):
    verbose_name = 'Специальность'
    verbose_name_plural = 'Специальности'

admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Content)
admin.site.register(Card)
