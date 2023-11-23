# notes/urls.py
from django.urls import path
from .views.views import OpenAIView



urlpatterns = [
    path('summarize/note/<int:note_id>', OpenAIView.as_view()),
]
