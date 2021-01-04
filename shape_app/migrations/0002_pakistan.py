# Generated by Django 3.1.4 on 2021-01-02 11:05

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shape_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pakistan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_0', models.BigIntegerField()),
                ('iso', models.CharField(max_length=3)),
                ('name_0', models.CharField(max_length=75)),
                ('id_1', models.BigIntegerField()),
                ('name_1', models.CharField(max_length=75)),
                ('id_2', models.BigIntegerField()),
                ('name_2', models.CharField(max_length=75)),
                ('id_3', models.BigIntegerField()),
                ('name_3', models.CharField(max_length=75)),
                ('type_3', models.CharField(max_length=50)),
                ('engtype_3', models.CharField(max_length=50)),
                ('nl_name_3', models.CharField(max_length=75)),
                ('varname_3', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
