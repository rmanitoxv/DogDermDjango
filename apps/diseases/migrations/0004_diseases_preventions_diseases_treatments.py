# Generated by Django 4.1.4 on 2023-01-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0003_remove_diseases_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseases',
            name='preventions',
            field=models.TextField(blank=True, default=None, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='diseases',
            name='treatments',
            field=models.TextField(blank=True, default=None, max_length=999, null=True),
        ),
    ]
