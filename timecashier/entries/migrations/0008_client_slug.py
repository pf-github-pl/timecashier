# Generated by Django 4.0.2 on 2022-02-12 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0007_entry_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
