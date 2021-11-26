from django.test import TestCase
from eventex.nucleo.models import Speaker
from django.shortcuts import resolve_url as r

class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hote-site',
            description='Programadora e almirante'
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_fields_can_be_blank(self):
        fields = ['description', 'website']
        for expected in fields:
            with self.subTest():
                field = Speaker._meta.get_field(expected)
                self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Grace Hopper', str(self.speaker))

    def test_get_absolute_url(self):
        url = r('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())
