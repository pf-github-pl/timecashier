# Generated by Django 4.0.2 on 2022-02-12 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0005_entry_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='clients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entry',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='entries.client'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='entries', to=settings.AUTH_USER_MODEL),
        ),
    ]