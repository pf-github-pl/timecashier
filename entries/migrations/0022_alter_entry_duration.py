# Generated by Django 4.0.2 on 2022-02-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0021_entry_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='duration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]