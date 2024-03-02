from django.contrib import admin
from .models import Professions, Promo, Task, Map, MapPointer, Card, Speciality

class ProfessionsAdmin(admin.ModelAdmin):
    verbose_name = 'Профессия'
    verbose_name_plural = 'Профессия'

admin.site.register(Professions, ProfessionsAdmin)
admin.site.register(Promo)
admin.site.register(Task)
admin.site.register(Map)
admin.site.register(MapPointer)
admin.site.register(Card)
admin.site.register(Speciality)
