from rest_framework import serializers
from .models import Speciality, Profession


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'name', 'description', 'link')


class SpecialitySerializer(serializers.ModelSerializer):
    professions = ProfessionSerializer(many=True, read_only=True, source='profession_set')

    class Meta:
        model = Speciality
        fields = ('id', 'tiker', 'color', 'code', 'name', 'professions')
