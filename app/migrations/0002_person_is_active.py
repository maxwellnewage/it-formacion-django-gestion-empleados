# Generated by Django 4.2 on 2023-04-25 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
