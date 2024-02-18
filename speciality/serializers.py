from rest_framework import serializers
from .models import Speciality, Content, Card

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('id', 'tab_id', 'tab_label')

class ContentSerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer()

    class Meta:
        model = Content
        fields = ('id', 'speciality', 'tags', 'text')

class CardSerializer(serializers.ModelSerializer):
    content = ContentSerializer()

    class Meta:
        model = Card
        fields = ('id', 'content', 'title', 'card_text', 'image')
