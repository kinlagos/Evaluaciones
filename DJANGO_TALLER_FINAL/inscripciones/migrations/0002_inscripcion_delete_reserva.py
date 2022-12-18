# Generated by Django 4.1.4 on 2022-12-14 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fono', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('institucion', models.CharField(max_length=30)),
                ('hora', models.TimeField()),
                ('estado', models.CharField(choices=[('RESERVADO', 'RESERVADO'), ('COMPLETADA', 'COMPLETADA'), ('ANULADA', 'ANULADA'), ('NO ASISTEN', 'NO ASISTEN')], max_length=20)),
                ('observacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='reserva',
        ),
    ]
