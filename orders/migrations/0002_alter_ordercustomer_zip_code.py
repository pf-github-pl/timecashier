# Generated by Django 4.0.2 on 2023-03-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercustomer',
            name='zip_code',
            field=models.CharField(max_length=6),
        ),
    ]
