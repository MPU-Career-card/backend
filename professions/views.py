from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Professions
from .serializers import ProfessionsSerializer
from speciality.models import Speciality, Profession
from speciality.serializers import SpecialitySerializer, ProfessionSerializer
from django.db.models import Q 


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

class SearchFacultiesView(APIView):
    def get(self, request, search_string=None):
        # Поиск специальностей и профессий, содержащих строку поиска
        specialities = Speciality.objects.filter(
            Q(name__icontains=search_string) |
            Q(profession__name__icontains=search_string) |  # Проверка связи с Profession
            Q(profession__description__icontains=search_string)
        ).distinct()

        professions_in_profession = Profession.objects.filter(
            Q(name__icontains=search_string) |
            Q(description__icontains=search_string)
        )

        # Получаем названия профессий из найденных объектов Profession
        profession_titles = professions_in_profession.values_list('name', flat=True)

        # Поиск профессий в модели Professions, у которых значение title соответствует найденным названиям профессий
        professions_in_professions = Professions.objects.filter(title__in=profession_titles)

        # Создаем словарь для хранения данных по факультетам
        faculties_data = {}

        # Добавляем профессии в словарь
        for profession in professions_in_professions:
            faculty = profession.faculty
            if faculty not in faculties_data:
                faculties_data[faculty] = {
                    'professions': [],
                    'specialities': []
                }
            # Создаем сериализатор для модели Professions и добавляем данные в словарь
            professions_data = ProfessionsSerializer(profession).data
            faculties_data[faculty]['professions'].append(professions_data)

        # Добавляем специальности в словарь
        for speciality in specialities:
            faculty = speciality.faculty
            if faculty not in faculties_data:
                faculties_data[faculty] = {
                    'professions': [],
                    'specialities': []
                }
            speciality_data = SpecialitySerializer(speciality).data

            # Добавляем профессии для каждой специальности
            professions_for_speciality = Profession.objects.filter(speciality=speciality)
            speciality_data['professions'] = ProfessionSerializer(professions_for_speciality, many=True).data

            faculties_data[faculty]['specialities'].append(speciality_data)

        return Response(faculties_data)
