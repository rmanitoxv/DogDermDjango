# Generated by Django 4.1.4 on 2022-12-08 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0004_clinics_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinics',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='url',
        ),
    ]
