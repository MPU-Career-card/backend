from django.contrib import admin
from .models import Professions, Promo, Task, Map, MapPointer, Card, Speciality
from import_export.admin import ImportExportMixin
from import_export import fields, resources
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from django.db import transaction
from import_export.instance_loaders import ModelInstanceLoader



class ProfessionsAdminResource(resources.ModelResource):
    tasks = fields.Field(
        column_name="Основные задачи",
        attribute="tasks",
        widget=ManyToManyWidget(Task, separator='\n\n')
    )
    id = fields.Field(column_name="ID", attribute="id", readonly=True)
    title = fields.Field(column_name="Название профессии", attribute="title")
    description = fields.Field(column_name="Описание профессии", attribute="description")
    tasks = fields.Field(column_name="Основные задачи", attribute="tasks")

    class Meta:
        model = Professions
        fields = ('id', 'title', 'description', 'tasks')
    
    @transaction.atomic
    def before_import_row(self, row, **kwargs):
        instance_loader = kwargs.get('instance_loader')
        profession_instance = instance_loader.get_instance()

        tasks_text = row.get('Основные задачи', '').strip()
        tasks_list = tasks_text.split('\n\n\n')
        tasks_instances = []

        for task_text in tasks_list:
            task_title, task_text = task_text.split('\n\n', 1) 
            task_instance = Task(title=task_title.strip(), text=task_text.strip(), profession=profession_instance)
            tasks_instances.append(task_instance)

        row['tasks'] = tasks_instances

class ProfessionsAdmin(ImportExportMixin, admin.ModelAdmin):
    verbose_name = 'Профессия'
    verbose_name_plural = 'Профессия'
    resource_class = ProfessionsAdminResource

admin.site.register(Professions, ProfessionsAdmin)
admin.site.register(Promo)
admin.site.register(Task)
admin.site.register(Map)
admin.site.register(MapPointer)
admin.site.register(Card)
admin.site.register(Speciality)
