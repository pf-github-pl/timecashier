# Generated by Django 4.0.2 on 2022-02-12 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_alter_entry_end_alter_entry_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]