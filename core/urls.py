"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from professions import views
from rest_framework import routers
from speciality.views import SpecialityViewSet
from professions.views import ProfessionsViewSet


router = routers.DefaultRouter()
router.register(r'professions', ProfessionsViewSet)
router.register(r'specialities', SpecialityViewSet)

urlpatterns = [
    path('professions/<str:title>/', views.ProfessionsViewSet.as_view(
        {'get': 'retrieve'}), name='get_profession_by_title'),
    path('faculties/', views.FacultiesListView.as_view(), name='get_all_faculties'),
    path('faculties/<str:faculty>/', views.FacultiesProfessionsView.as_view(),
         name='get_professions_by_faculty'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
