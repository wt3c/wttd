from django.db import models

class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('Telefone', max_length=20)
    created_at = models.DateTimeField('Criando em', auto_now_add=True)
    paid = models.BooleanField('Pago', default=False)

    class Meta:
        verbose_name = 'incrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
