# Generated by Django 4.1 on 2022-08-08 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_rename_monthlysummary_resumo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumo',
            name='teste',
        ),
    ]
