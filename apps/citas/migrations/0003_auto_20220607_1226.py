# Generated by Django 3.2 on 2022-06-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_auto_20220607_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallecitaservicio',
            options={'verbose_name': 'Detalle de Cita-Servicio', 'verbose_name_plural': 'Detalle de Citas-Servicios'},
        ),
        migrations.AlterField(
            model_name='cita',
            name='id_numero_cita',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]