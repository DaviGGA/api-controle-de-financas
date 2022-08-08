# Generated by Django 4.1 on 2022-08-08 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_resumo_despesas_alter_resumo_receitas'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumoMensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.FloatField()),
                ('gasto_categoria', models.FloatField()),
                ('despesas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.despesa')),
                ('receitas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.receita')),
            ],
        ),
        migrations.DeleteModel(
            name='Resumo',
        ),
    ]
