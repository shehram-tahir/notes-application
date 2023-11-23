# notes/views.py
from rest_framework import viewsets
from ..models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.filter(is_active=True)
    serializer_class = NoteSerializer
    # permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
