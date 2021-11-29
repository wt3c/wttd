from django.test import TestCase
from eventex.nucleo.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra',
            start='10:00',
            description='Descrição da palestra.'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_spearkers(self):
        """Talk has many Speakers and vice-versa"""
        self.talk.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_talk_fields_blank(self):
        fields = ['speakers', 'start', 'description']
        for field in fields:
            with self.subTest():
                expected = Talk._meta.get_field('{}'.format(field))
                self.assertTrue(expected.blank)
