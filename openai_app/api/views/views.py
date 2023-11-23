from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers.note_summarizer import NoteSerializer
from ..utils.openai_utils import get_note_summarization


class OpenAIView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get(self, request, **kwargs):
        """
        Returns the summarized note text

        Parameters:
                request:
                kwargs:
         Returns:
                Text (str): Summarized text
        """
        serilizer = self.get_serializer(data=kwargs)
        serilizer.is_valid(raise_exception=True)
        summarized_note = get_note_summarization(serilizer.validated_data.get('note_id').content)
        return Response({'summarized_note': summarized_note})
