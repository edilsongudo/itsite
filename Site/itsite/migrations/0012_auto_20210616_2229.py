# Generated by Django 3.0 on 2021-06-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsite', '0011_auto_20210616_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]