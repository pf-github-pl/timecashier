# Generated by Django 4.0.2 on 2022-02-12 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0008_client_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]