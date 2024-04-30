from rest_framework import serializers
from .models import Professions, Task, Tag, MapPointer, Skill, Bachelor, Master, FurtherEducation, HHVacancy, Partners, UsefulLink


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class MapPointerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPointer
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class BachelorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bachelor
        fields = '__all__'


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class FurtherEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurtherEducation
        fields = '__all__'


class HHVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = HHVacancy
        fields = '__all__'


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


class UsefulLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLink
        fields = '__all__'


class ProfessionsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True, source='tag_set')
    tasks = TaskSerializer(many=True, read_only=True, source='task_set')
    map_pointers = MapPointerSerializer(many=True, read_only=True, source='mappointer_set')
    skills = SkillSerializer(many=True, read_only=True, source='skill_set')
    bachelors = BachelorSerializer(many=True, read_only=True, source='bachelor_set')
    masters = MasterSerializer(many=True, read_only=True, source='master_set')
    further_educations = FurtherEducationSerializer(many=True, read_only=True, source='furthereducation_set')
    hh_vacancies = HHVacancySerializer(many=True, read_only=True, source='hhvacancy_set')  
    partners = PartnersSerializer(many=True, read_only=True, source='partners_set')
    useful_links = UsefulLinkSerializer(many=True, read_only=True, source='usefullink_set')

    class Meta:
        model = Professions
        fields = ('id', 'title', 'image_link', 'faculty', 'description', 'tags',
                  'tasks', 'map_pointers','skills', 'bachelors', 'masters',
                  'further_educations', 'hh_vacancies', 'partners', 'useful_links')
