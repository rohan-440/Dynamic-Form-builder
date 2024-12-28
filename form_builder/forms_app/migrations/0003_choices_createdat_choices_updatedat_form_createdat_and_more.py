# Generated by Django 5.0.7 on 2024-12-28 15:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0002_question_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choices',
            name='createdAt',
            field=models.DateField(auto_now_add=True, default='2024-12-28 00:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choices',
            name='updatedAt',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='form',
            name='createdAt',
            field=models.DateField(auto_now_add=True, default='2024-12-28 00:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='updatedAt',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='createdAt',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='updatedAt',
            field=models.DateField(auto_now=True),
        ),
    ]
