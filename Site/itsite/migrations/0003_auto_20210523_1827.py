# Generated by Django 3.0 on 2021-05-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsite', '0002_auto_20210523_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applymodel',
            old_name='linked_in_profile',
            new_name='linkedin_profile_url',
        ),
        migrations.AddField(
            model_name='applymodel',
            name='github_profile_url',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='applymodel',
            name='cv',
            field=models.FileField(upload_to='cvs'),
        ),
    ]
