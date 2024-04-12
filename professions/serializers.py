from rest_framework import serializers
from .models import Professions, Promo, Task, MapPointer, Card, Speciality


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

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'

class ProfessionsSerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer(many=True, read_only=True)
    promos = PromoSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Professions
        fields = '__all__'