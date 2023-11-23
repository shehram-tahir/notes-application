# notes/urls.py
from django.urls import path, include


urlpatterns = [
    path('api/', include(('notes.api.urls', 'notes'), namespace='api', ))
]
