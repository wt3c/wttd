from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribeEmail(TestCase):
    def setUp(self):
        data = dict(name='Welington Carlos', cpf='12345678901', email='carlos@gmail.com', phone='2198985-6652')
        self.resp = self.client.post(r('subscriptions:new'), data)
        # print(mail.outbox[0])
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
            '12345678901',
            'carlos@gmail.com',
            '2198985-6652',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
