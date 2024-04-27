from django.contrib import admin
from .models import Speciality, Profession
from import_export.admin import ImportExportMixin
from import_export import fields, resources
from professions.admin import BLOCK_SEPARATOR, COMPONENT_SEPARATOR


class SpecialityAdminResource(resources.ModelResource):
    tiker = fields.Field(column_name='Тикер', attribute='tiker')
    color = fields.Field(column_name='Цвет тикера', attribute='color')
    code = fields.Field(column_name='Код направления', attribute='code')
    name = fields.Field(column_name='Название направления', attribute='name')

    class Meta:
        model = Speciality
        skip_unchanged = True
        report_skipped = False
        fields = ('code')
        import_id_fields = ('code',)

    def after_import_row(self, row, row_result, row_number=None, **kwargs):
        speciality_code = row.get('Код направления', '').strip()
        speciality_instance = Speciality.objects.get(code=speciality_code)

        # Professions
        professions_text = row.get('Профессии',' ').strip()
        professions_list = professions_text.split(BLOCK_SEPARATOR)
        professions_instances = []
        for profession_text in professions_list:
            profession_name, profession_description = profession_text.split(COMPONENT_SEPARATOR, 1)
            profession_instance, _ = Profession.objects.get_or_create(name=profession_name.strip(),
                                                                      description=profession_description,
                                                                      speciality=speciality_instance)
            professions_instances.append(profession_instance)
        row['professions'] = professions_instances


class SpecialityAdmin(ImportExportMixin, admin.ModelAdmin):
    verbose_name = 'Специальность'
    verbose_name_plural = 'Специальности'
    resource_class = SpecialityAdminResource


admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Profession)
