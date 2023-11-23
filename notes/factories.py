import factory
from notes.models import Note


class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note

    title = factory.Faker('sentence')
    content = factory.Faker('text')
