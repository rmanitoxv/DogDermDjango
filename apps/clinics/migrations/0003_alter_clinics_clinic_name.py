# Generated by Django 4.1.4 on 2022-12-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0002_rename_clinic_clinics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinics',
            name='clinic_name',
            field=models.TextField(unique=True),
        ),
    ]
