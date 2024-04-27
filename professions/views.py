from rest_framework import viewsets
from rest_framework.response import Response
from .models import Professions
from .serializers import ProfessionsSerializer
from django.http import Http404


class ProfessionsViewSet(viewsets.ModelViewSet):
    queryset = Professions.objects.all()
    serializer_class = ProfessionsSerializer

    def retrieve(self, request, title=None):
        try:
            profession = Professions.objects.get(title=title)
        except Professions.DoesNotExist:
            raise Http404

        serializer = ProfessionsSerializer(profession)
        return Response(serializer.data)
