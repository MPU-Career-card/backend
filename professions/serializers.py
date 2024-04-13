from rest_framework import serializers
from .models import Professions, Promo, Task, Card, Speciality, Tag, MapPointer, Skill, Bakalavr, Magistr, DPO, HHVacancy, Partners, UsefulLink

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'

class MapPointerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPointer
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class BakalavrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bakalavr
        fields = '__all__'

class MagistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magistr
        fields = '__all__'

class DPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = DPO
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
    tags = TagSerializer(many=True, read_only=True)
    promos = PromoSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    cards = CardSerializer(many=True, read_only=True)
    specialities = SpecialitySerializer(many=True, read_only=True, source='speciality_set')
    map_pointers = MapPointerSerializer(many=True, read_only=True, source='mappointer_set')
    skills = SkillSerializer(many=True, read_only=True, source='skill_set')
    bakalavrs = BakalavrSerializer(many=True, read_only=True, source='bakalavr_set')
    magistrs = MagistrSerializer(many=True, read_only=True, source='magistr_set')
    dpos = DPOSerializer(many=True, read_only=True, source='dpo_set')
    hh_vacancies = HHVacancySerializer(many=True, read_only=True, source='hhvacancy_set')  
    partners = PartnersSerializer(many=True, read_only=True, source='partners_set')
    useful_links = UsefulLinkSerializer(many=True, read_only=True, source='usefullink_set')

    class Meta:
        model = Professions
        fields = ('id', 'title', 'tags', 'promos', 'tasks', 'cards', 'specialities', 'map_pointers', 'skills', 'bakalavrs', 'magistrs', 'dpos', 'hh_vacancies', 'partners', 'useful_links')
