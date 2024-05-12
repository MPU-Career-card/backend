from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Professions
from .serializers import ProfessionsSerializer
from speciality.models import Speciality
from speciality.serializers import SpecialitySerializer 


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


class FacultiesListView(APIView):
    def get(self, request):
        faculties = Professions.objects.values_list('faculty', flat=True).distinct()
        return Response(faculties)

class FacultiesProfessionsView(APIView):
    def get(self, request, faculty=None):
        professions = Professions.objects.filter(faculty=faculty)
        professions_serializer = ProfessionsSerializer(professions, many=True)
        specialities = Speciality.objects.filter(faculty=faculty)
        specialities_serializer = SpecialitySerializer(specialities, many=True)
        data = {
            'professions': professions_serializer.data,
            'specialities': specialities_serializer.data
        }
        
        return Response(data)
