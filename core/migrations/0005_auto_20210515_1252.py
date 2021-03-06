# Generated by Django 3.2.3 on 2021-05-15 15:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_audiencia_emissora_audiencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiencia',
            name='data_hora_audiencia',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data e Hora da Audiência'),
        ),
        migrations.AlterField(
            model_name='audiencia',
            name='emissora_audiencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.emissora', verbose_name='Emissora'),
        ),
    ]
