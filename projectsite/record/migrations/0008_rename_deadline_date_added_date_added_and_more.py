# Generated by Django 5.0 on 2023-12-29 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0007_remove_artist_department_remove_duration_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date_added',
            old_name='Deadline',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='duration',
            old_name='durationName',
            new_name='songsName',
        ),
    ]
