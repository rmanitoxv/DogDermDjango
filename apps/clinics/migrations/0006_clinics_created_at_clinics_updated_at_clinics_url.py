# Generated by Django 4.1.4 on 2022-12-08 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0005_remove_clinics_created_at_remove_clinics_deleted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinics',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinics',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='clinics',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]