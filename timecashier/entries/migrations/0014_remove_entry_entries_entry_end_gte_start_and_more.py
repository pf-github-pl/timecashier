# Generated by Django 4.0.2 on 2022-02-14 22:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0013_alter_entry_tags'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='entry',
            name='entries_entry_end_gte_start',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='end',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='start',
        ),
        migrations.AddField(
            model_name='entry',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='start_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='start_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]