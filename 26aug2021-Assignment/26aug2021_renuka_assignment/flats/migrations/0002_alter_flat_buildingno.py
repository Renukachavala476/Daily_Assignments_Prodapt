# Generated by Django 3.2.6 on 2021-08-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='BuildingNo',
            field=models.CharField(max_length=50),
        ),
    ]
