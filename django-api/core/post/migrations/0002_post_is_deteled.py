# Generated by Django 4.0 on 2024-04-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_deteled',
            field=models.BooleanField(default=False),
        ),
    ]