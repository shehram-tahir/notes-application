# notes/views.py
from rest_framework import viewsets
from ..models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated


class NoteViewSet(viewsets.ModelViewSet):
    """View to perform CRUD operations on  Notes"""
    queryset = Note.objects.filter(is_active=True)
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        """
        This is to deactivate notes instead of deleting
        Parameters:
                instance:
        """
        instance.is_active = False
        instance.save()
