# Generated by Django 3.2.3 on 2021-05-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_audiencia_pontos_audiencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiencia',
            name='emissora_audiencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.emissora', unique_for_date='Emissora', verbose_name='Emissora'),
        ),
    ]
