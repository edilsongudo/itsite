# Generated by Django 3.0 on 2021-06-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsite', '0009_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
