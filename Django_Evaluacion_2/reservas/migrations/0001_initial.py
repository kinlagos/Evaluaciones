# Generated by Django 4.1.1 on 2022-10-27 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fono', models.CharField(max_length=20)),
                ('fechareserva', models.DateField()),
                ('horareserva', models.DateTimeField()),
                ('contpersona', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
                ('observacion', models.CharField(max_length=200)),
            ],
        ),
    ]
