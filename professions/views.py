from rest_framework import viewsets
from .models import Professions
from .serializers import ProfessionsSerializer

class ProfessionsViewSet(viewsets.ModelViewSet):
    queryset = Professions.objects.all()
    serializer_class = ProfessionsSerializer
