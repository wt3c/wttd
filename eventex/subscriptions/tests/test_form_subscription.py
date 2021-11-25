from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPFs must only accpet digits."""
        form = self.make_validated_form(cpf='1234abcd')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPFs must have 11 digits."""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self,form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        erros_list = errors[field]
        self.assertListEqual([msg], erros_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Welington Carlos',
                     cpf='12345678901',
                     email='carlos@gamil.com',
                     phone='21-986186180')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
