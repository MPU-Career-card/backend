from django.contrib import admin
from .models import Professions, Tag, Promo, Task, Map, MapPointer, Card, Speciality
from import_export.admin import ImportExportMixin
from import_export import fields, resources, widgets

BLOCK_SEPARATOR = '$'
COMPONENT_SEPARATOR = '|'

class ProfessionsAdminResource(resources.ModelResource):
    title = fields.Field(column_name="Название профессии", attribute="title")
    description = fields.Field(column_name="Описание профессии", attribute="description")
    tasks = fields.Field(
        column_name='Задачи',
        attribute='task',
        widget=widgets.ForeignKeyWidget(Task, 'profession')
    )

    class Meta:
        model = Professions
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'title', 'tags', 'description', 'tasks')
        
    def after_import_row(self, row, row_result, row_number=None, **kwargs):
        profession_title = row.get('Название профессии', '').strip()
        profession_instance = Professions.objects.get(title=profession_title)

        # tags - не получается добавить как ForeignKeyWidget, но так работает; возможно стоит убрать и tasks
        tags_text = row.get('Тэги', '').strip()
        tags_list = tags_text.split(BLOCK_SEPARATOR)
        tags_instances = []
        for tag_name in tags_list:
            task_instance, _ = Tag.objects.get_or_create(name=tag_name.strip(), profession=profession_instance)
            tags_instances.append(task_instance)
        row['tags'] = tags_instances

        # tasks
        tasks_text = row.get('Основные задачи', '').strip()
        tasks_list = tasks_text.split(BLOCK_SEPARATOR)
        tasks_instances = []
        for task_text in tasks_list:
            task_title, task_text = task_text.split(COMPONENT_SEPARATOR, 1)
            task_instance, _ = Task.objects.get_or_create(title=task_title.strip(), text=task_text.strip(), profession=profession_instance)
            tasks_instances.append(task_instance)
        row['tasks'] = tasks_instances

class ProfessionsAdmin(ImportExportMixin, admin.ModelAdmin):
    verbose_name = 'Профессия'
    verbose_name_plural = 'Профессия'
    resource_class = ProfessionsAdminResource

admin.site.register(Professions, ProfessionsAdmin)
admin.site.register(Tag, ProfessionsAdmin)
admin.site.register(Promo)
admin.site.register(Task)
admin.site.register(Map)
admin.site.register(MapPointer)
admin.site.register(Card)
admin.site.register(Speciality)
