from rest_framework import generics, permissions, filters
from . import serializers
from main.models import Note, Category
from django.contrib.auth.models import User
from .permisisions import IsOwnerFilterBackend

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer
    filter_backends = [IsOwnerFilterBackend]

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [IsOwnerFilterBackend]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser]