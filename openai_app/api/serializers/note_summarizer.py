from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.Serializer):

    note_id = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all(), required=True)
