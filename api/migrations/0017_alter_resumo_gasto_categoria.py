# Generated by Django 4.1 on 2022-08-08 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_resumo_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumo',
            name='gasto_categoria',
            field=models.TextField(),
        ),
    ]