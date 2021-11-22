from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribePost(TestCase):
    def setUp(self):
        data = dict(name='Welington Carlos', cpf='123456789101', email='carlos@gmail.com', phone='2198985-6652')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_post(self):
        """Valid POST should redirect to /inscicao"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = ['contato@eventex.com.br', 'carlos@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_suscription_email_body(self):
        contents = [
            'Welington Carlos',
            '123456789101',
            'carlos@gmail.com',
            '2198985-6652',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
