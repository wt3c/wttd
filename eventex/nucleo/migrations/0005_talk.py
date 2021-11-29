# Generated by Django 3.2.9 on 2021-11-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0004_auto_20211126_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start', models.TimeField()),
                ('description', models.TextField()),
                ('speakers', models.ManyToManyField(to='nucleo.Speaker')),
            ],
        ),
    ]
