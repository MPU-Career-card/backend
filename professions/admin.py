from django.contrib import admin
from .models import Professions, Tag, Task, MapPointer, Skill, Bachelor, Master, FurtherEducation, HHVacancy, Partners, UsefulLink
from import_export.admin import ImportExportMixin
from import_export import fields, resources

BLOCK_SEPARATOR = '$'
COMPONENT_SEPARATOR = '|'


class ProfessionsAdminResource(resources.ModelResource):
    title = fields.Field(column_name="Название профессии", attribute="title")
    faculty = fields.Field(column_name="Факультет", attribute="faculty")
    description = fields.Field(column_name="Описание профессии", attribute="description")
    image_link = fields.Field(column_name="Главное изображение", attribute="image_link")

    class Meta:
        model = Professions
        skip_unchanged = True
        report_skipped = False
        fields = ('title')
        import_id_fields = ('title',)
    
    def after_import_row(self, row, row_result, row_number=None, **kwargs):
        profession_title = row.get('Название профессии', '').strip()
        profession_instance = Professions.objects.get(title=profession_title)
        faculty = row.get('Факультет', '').strip()

        # Tags
        tags_text = row.get('Тэги', '').strip()
        tags_list = tags_text.split(BLOCK_SEPARATOR)
        tags_instances = []
        for tag_name in tags_list:
            task_instance, _ = Tag.objects.get_or_create(name=tag_name.strip(),
                                                         profession=profession_instance)
            tags_instances.append(task_instance)
        row['tags'] = tags_instances

        # Tasks
        tasks_text = row.get('Основные задачи', '').strip()
        tasks_list = tasks_text.split(BLOCK_SEPARATOR)
        tasks_instances = []
        for task_text in tasks_list:
            task_title, task_text = task_text.split(COMPONENT_SEPARATOR, 1)
            task_instance, _ = Task.objects.get_or_create(title=task_title.strip(),
                                                          text=task_text.strip(),
                                                          profession=profession_instance)
            tasks_instances.append(task_instance)
        row['tasks'] = tasks_instances

        # Map
        map_text = row.get('Карьерный путь', '').strip()
        map_list = map_text.split(BLOCK_SEPARATOR)
        map_instances = []
        for map_text in map_list:
            map_title, map_text, map_salary = map_text.split(COMPONENT_SEPARATOR, 2)
            map_instance, _ = MapPointer.objects.get_or_create(title=map_title.strip(),
                                                               description=map_text.strip(),
                                                               salary=map_salary.strip(),
                                                               profession=profession_instance)
            map_instances.append(map_instance)
        row['map'] = map_instances
        
        # Skills
        skills_text = row.get('Необходимые навыки', '').strip()
        skills_list = skills_text.split(BLOCK_SEPARATOR)
        skills_instances = []
        for skills_text in skills_list:
            skills_name, skills_text, image_link = skills_text.split(COMPONENT_SEPARATOR, 2)
            skills_instance, _ = Skill.objects.get_or_create(name=skills_name.strip(),
                                                             description=skills_text.strip(),
                                                             image_link=image_link.strip(),
                                                             profession=profession_instance)
            skills_instances.append(skills_instance)
        row['skills'] = skills_instances

        # Bachelor
        bachelor_text = row.get('Бакалавр', '').strip()
        bachelor_list = bachelor_text.split(BLOCK_SEPARATOR)
        bachelor_instances = []
        for bachelor_text in bachelor_list:
            bachelor_speciality_name, bachelor_link = bachelor_text.split(COMPONENT_SEPARATOR, 1)
            bachelor_instance, _ = Bachelor.objects.get_or_create(faculty_name=faculty,
                                                                  speciality_name=bachelor_speciality_name.strip(),
                                                                  link=bachelor_link,
                                                                  profession=profession_instance)
            bachelor_instances.append(bachelor_instance)
        row['bachelor'] = bachelor_instances

        # Master
        if row.get('Магистратура', '') != None:
            master_text = row.get('Магистратура',' ').strip()
            master_list = master_text.split(BLOCK_SEPARATOR)
            master_instances = []
            for master_text in master_list:
                master_speciality_name, master_link = master_text.split(COMPONENT_SEPARATOR, 1)
                master_instance, _ = Master.objects.get_or_create(faculty_name=faculty,
                                                                    speciality_name=master_speciality_name.strip(),
                                                                    link=master_link,
                                                                    profession=profession_instance)
                master_instances.append(master_instance)
            row['master'] = master_instances
        else:
            row['master'] = None

        # FurtherEducation
        if row.get('ДПО', '') != None:
            fe_text = row.get('ДПО', '').strip()
            fe_list = fe_text.split(BLOCK_SEPARATOR)
            fe_instances = []
            for fe_text in fe_list:
                fe_speciality_name, fe_link = fe_text.split(COMPONENT_SEPARATOR, 1)
                fe_instance, _ = FurtherEducation.objects.get_or_create(faculty_name=faculty, 
                                                                         speciality_name=fe_speciality_name.strip(),
                                                                         link=fe_link,
                                                                         profession=profession_instance)
                fe_instances.append(fe_instance)
            row['further_education'] = fe_instances
        else:
            row['further_education'] = None

        # HHVacancy
        hhvacancy_text = row.get('hh', '').strip()
        row['hh'] = hhvacancy_text

        # Partners
        if row.get('Партнеры', '') != None:
            partners_text = row.get('Партнеры',' ').strip()
            partners_list = partners_text.split(BLOCK_SEPARATOR)
            partners_instances = []
            for partners_text in partners_list:
                partners_name, partners_link, partners_image = partners_text.split(COMPONENT_SEPARATOR, 2)
                partners_instance, _ = Partners.objects.get_or_create(name=partners_name.strip(),
                                                                    link=partners_link,
                                                                    image_link=partners_image,
                                                                    profession=profession_instance)
                partners_instances.append(partners_instance)
            row['partners'] = partners_instances

        # UsefulLink
        if row.get('Полезные ссылки', '') != None:
            useful_text = row.get('Полезные ссылки', '').strip()
            useful_list = useful_text.split(BLOCK_SEPARATOR)
            useful_instances = []
            for useful_text in useful_list:
                useful_name, useful_description, useful_link = useful_text.split(COMPONENT_SEPARATOR, 2)
                useful_instance, _ = UsefulLink.objects.get_or_create(name=useful_name.strip(),
                                                                    description=useful_description,
                                                                    link=useful_link,
                                                                    profession=profession_instance)
                useful_instances.append(useful_instance)
            row['useful'] = useful_instances


class ProfessionsAdmin(ImportExportMixin, admin.ModelAdmin):
    verbose_name = 'Профессия'
    verbose_name_plural = 'Профессия'
    resource_class = ProfessionsAdminResource


admin.site.register(Professions, ProfessionsAdmin)
admin.site.register(Tag, ProfessionsAdmin)
admin.site.register(Task)
admin.site.register(MapPointer)
admin.site.register(Skill)
admin.site.register(Bachelor)
admin.site.register(Master)
admin.site.register(FurtherEducation)
admin.site.register(HHVacancy)
admin.site.register(Partners)
admin.site.register(UsefulLink)
