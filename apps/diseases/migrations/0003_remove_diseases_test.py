# Generated by Django 4.1.4 on 2022-12-08 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0002_diseases_test_alter_diseases_causes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseases',
            name='test',
        ),
    ]