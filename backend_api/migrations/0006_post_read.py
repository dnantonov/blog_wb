# Generated by Django 3.2.9 on 2021-11-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0005_auto_20211112_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
