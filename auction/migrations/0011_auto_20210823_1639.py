# Generated by Django 3.1.7 on 2021-08-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_auto_20210822_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('BOAT', 'Boat'), ('CARAVAN', 'Caravan'), ('CAR', 'Car')], default='BOAT', max_length=8, verbose_name='Vehicle Type'),
        ),
    ]
