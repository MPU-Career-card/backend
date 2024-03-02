from rest_framework import serializers
from .models import Professions, Promo, Task, Map, MapPointer, Card, Speciality

class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        fields = '__all__'

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class MapPointerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPointer
        fields = '__all__'

class MapSerializer(serializers.ModelSerializer):
    pointers = MapPointerSerializer(many=True, read_only=True)

    class Meta:
        model = Map
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'
