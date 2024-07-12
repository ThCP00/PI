# Generated by Django 5.0.7 on 2024-07-12 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queimadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataHora', models.DateTimeField(default=datetime.datetime.now)),
                ('Satelite', models.CharField(max_length=100)),
                ('Pais', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=100)),
                ('Municipio', models.CharField(max_length=100)),
                ('Bioma', models.CharField(max_length=100)),
                ('DiaSemChuva', models.IntegerField()),
                ('Precipitacao', models.FloatField()),
                ('RiscoFogo', models.FloatField()),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('FRP', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
