# Generated by Django 3.2.9 on 2021-11-26 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('website', models.URLField()),
                ('photo', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]