# Generated by Django 4.1.4 on 2023-01-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_verified_at',
        ),
        migrations.AddField(
            model_name='user',
            name='email_verification',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]