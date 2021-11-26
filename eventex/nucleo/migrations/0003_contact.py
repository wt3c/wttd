# Generated by Django 3.2.9 on 2021-11-26 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0002_auto_20211126_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('E', 'Email'), ('P', 'Telefone')], max_length=1, verbose_name='Tipo')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.speaker')),
            ],
        ),
    ]
