# Generated by Django 4.0.2 on 2022-02-16 18:54

from django.db import migrations, models
import django.db.models.expressions
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0017_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='start_time',
        ),
        migrations.AddField(
            model_name='entry',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddConstraint(
            model_name='entry',
            constraint=models.CheckConstraint(check=models.Q(('end__gte', django.db.models.expressions.F('start'))), name='entries_entry_end_gte_start'),
        ),
    ]
