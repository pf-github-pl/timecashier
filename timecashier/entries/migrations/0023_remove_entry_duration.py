# Generated by Django 4.0.2 on 2022-02-18 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0022_alter_entry_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='duration',
        ),
    ]