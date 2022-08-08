# Generated by Django 4.1 on 2022-08-08 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_despesa_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('despesas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.despesa')),
                ('receitas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.receita')),
            ],
        ),
    ]
