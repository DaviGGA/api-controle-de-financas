# Generated by Django 4.1 on 2022-08-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_summary_delete_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='despesas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='receitas',
            field=models.FloatField(),
        ),
    ]