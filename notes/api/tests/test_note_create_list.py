import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_note_create_view(client):
    """Create note"""
    note_data = {
        'title': 'Test Note',
        'content': 'This is a test note.',
    }
    url = reverse('notes:api:notes-list')
    response = client.post(url, note_data, format='json')
    assert response.status_code == 201
    assert response.data['title'] == note_data['title']
