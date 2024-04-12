import openpyxl 
from django.contrib import admin
from .models import Professions, Tag, Promo, Task, MapPointer, Card, Speciality,Skill,Bakalavr,Magistr,DPO,HHVacancy,Partners,UsefulLink
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

        #map
        map_text = row.get('Карьерный путь',' ').strip()
        map_list = map_text.split(BLOCK_SEPARATOR)
        map_instances = []
        for map_text in map_list:
            map_title, map_text,map_salary = map_text.split(COMPONENT_SEPARATOR, 2)
            map_instance, _ = MapPointer.objects.get_or_create(title=map_title.strip(), description=map_text.strip(),salary=map_salary.strip(), profession=profession_instance)
            map_instances.append(map_instance)
        row['map'] = map_instances
        
        #skills
        skills_text = row.get('Необходимые навыки',' ').strip()
        skills_list = skills_text.split(BLOCK_SEPARATOR)
        skills_instances = []
        for skills_text in skills_list:
            skills_name, skills_text,svg = skills_text.split(COMPONENT_SEPARATOR, 2)
            skills_instance, _ = Skill.objects.get_or_create(name=skills_name.strip(), description=skills_text.strip(),svg=svg.strip(), profession=profession_instance)
            skills_instances.append(skills_instance)
        row['skills'] = skills_instances

        #bakalavr
        bakalavr_text = row.get('Бакалавр',' ').strip()
        bakalavr_list = bakalavr_text.split(BLOCK_SEPARATOR)
        bakalavr_instances = []
        for bakalavr_text in bakalavr_list:
            bakalavr_faculty_name, bakalavr_speciality_name,bakalavr_link = bakalavr_text.split(COMPONENT_SEPARATOR, 2)
            bakalavr_instance, _ = Bakalavr.objects.get_or_create(faculty_name=bakalavr_faculty_name.strip(), speciality_name=bakalavr_speciality_name.strip(),link=bakalavr_link, profession=profession_instance)
            bakalavr_instances.append(bakalavr_instance)
        row['bakalavr'] = bakalavr_instances

        #magistr
        if row.get('Магистратура',' ') != None:
            magistr_text = row.get('Магистратура',' ').strip()
            magistr_list = magistr_text.split(BLOCK_SEPARATOR)
            magistr_instances = []
            for magistr_text in magistr_list:
                magistr_faculty_name, magistr_speciality_name,magistr_link = magistr_text.split(COMPONENT_SEPARATOR, 2)
                magistr_instance, _ = Magistr.objects.get_or_create(faculty_name=magistr_faculty_name.strip(), speciality_name=magistr_speciality_name.strip(),link=magistr_link, profession=profession_instance)
                magistr_instances.append(magistr_instance)
            row['magistr'] = magistr_instances
        else:
            row['magistr'] = None
        #DPO
        if row.get('ДПО',' ') != None:
            dpo_text = row.get('ДПО',' ').strip()
            dpo_list = dpo_text.split(BLOCK_SEPARATOR)
            dpo_instances = []
            for dpo_text in dpo_list:
                dpo_faculty_name, dpo_speciality_name,dpo_link = dpo_text.split(COMPONENT_SEPARATOR, 2)
                dpo_instance, _ = DPO.objects.get_or_create(faculty_name=dpo_faculty_name.strip(), speciality_name=dpo_speciality_name.strip(),link=dpo_link, profession=profession_instance)
                dpo_instances.append(dpo_instance)
            row['dpo'] = dpo_instances
        else:
            row['dpo'] = None
        #HHVacancy
        hhvacancy_text = row.get('hh',' ').strip()
        row['hh'] = hhvacancy_text
        #partners
        partners_text = row.get('Партнеры',' ').strip()
        partners_list = partners_text.split(BLOCK_SEPARATOR)
        partners_instances = []
        for partners_text in partners_list:
            partners_name, partners_link = partners_text.split(COMPONENT_SEPARATOR, 1)
            partners_instance, _ = Partners.objects.get_or_create(name=partners_name.strip(), link=partners_link, profession=profession_instance)
            partners_instances.append(partners_instance)
        row['partners'] = partners_instances
        #UsefulLink
        useful_text = row.get('Полезные ссылки',' ').strip()
        useful_list = useful_text.split(BLOCK_SEPARATOR)
        useful_instances = []
        for useful_text in useful_list:
            useful_name, useful_link = useful_text.split(COMPONENT_SEPARATOR, 1)
            useful_instance, _ = UsefulLink.objects.get_or_create(name=useful_name.strip(), link=useful_link, profession=profession_instance)
            useful_instances.append(useful_instance)
        row['useful'] = useful_instances
class ProfessionsAdmin(ImportExportMixin, admin.ModelAdmin):
    verbose_name = 'Профессия'
    verbose_name_plural = 'Профессия'
    resource_class = ProfessionsAdminResource

admin.site.register(Professions, ProfessionsAdmin)
admin.site.register(Tag, ProfessionsAdmin)
admin.site.register(Promo)
admin.site.register(Task)
admin.site.register(MapPointer)
admin.site.register(Skill)
admin.site.register(Bakalavr)
admin.site.register(Magistr)
admin.site.register(DPO)
admin.site.register(HHVacancy)
admin.site.register(Partners)
admin.site.register(UsefulLink)
admin.site.register(Card)
admin.site.register(Speciality)
