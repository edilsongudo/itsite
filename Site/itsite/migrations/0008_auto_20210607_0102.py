# Generated by Django 3.0 on 2021-06-06 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsite', '0007_auto_20210524_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applymodel',
            name='github_profile_url',
        ),
        migrations.RemoveField(
            model_name='applymodel',
            name='linkedin_profile_url',
        ),
        migrations.AddField(
            model_name='applymodel',
            name='github_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applymodel',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
