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
from rest_framework import routers
from speciality.views import SpecialityViewSet, ContentViewSet, CardViewSet
from professions.views import ProfessionsViewSet, PromoViewSet, TaskViewSet, MapPointerViewSet, MapViewSet, CardProfViewSet, SpecialityProfViewSet


router = routers.DefaultRouter()
router.register(r'specialities', SpecialityViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'cards', CardViewSet)

router.register(r'professions', ProfessionsViewSet)
router.register(r'promo', PromoViewSet)
router.register(r'task', TaskViewSet)
router.register(r'mapPointer', MapPointerViewSet)
router.register(r'map', MapViewSet)
router.register(r'card', CardProfViewSet)
router.register(r'speciality', SpecialityProfViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

