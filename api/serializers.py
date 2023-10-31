from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'category_id', 'authors']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'authors']