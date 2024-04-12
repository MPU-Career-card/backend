from rest_framework import viewsets
from .models import Professions, Promo, Task, MapPointer, Card, Speciality
from .serializers import ProfessionsSerializer, PromoSerializer, TaskSerializer, MapPointerSerializer, CardSerializer, SpecialitySerializer

class ProfessionsViewSet(viewsets.ModelViewSet):
    queryset = Professions.objects.all()
    serializer_class = ProfessionsSerializer

class PromoViewSet(viewsets.ModelViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class MapPointerViewSet(viewsets.ModelViewSet):
    queryset = MapPointer.objects.all()
    serializer_class = MapPointerSerializer

class CardProfViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class SpecialityProfViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
