# Generated by Django 4.2.4 on 2023-08-10 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel_lister', '0002_rename_destinations_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]