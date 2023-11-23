from rest_framework.test import APIClient
import pytest
from rest_framework.reverse import reverse
from notes.models import Note

# client = APIClient()


@pytest.mark.django_db
def test_note_list_create_view(client):
    note_data = {
        'title': 'Test Note',
        'content': 'This is a test note.',
    }
    url = reverse('notes:api:notes-list')
    response = client.post(url, note_data, format='json')
    assert response.status_code == 201
    assert response.data['title'] == note_data['title']
