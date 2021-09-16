# Generated by Django 3.1.7 on 2021-09-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0024_auto_20210901_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='auctionVehicleType',
            field=models.CharField(choices=[('BOAT', 'Boat'), ('CARAVAN', 'Caravan'), ('CAR', 'Car'), ('TINYHOUSE', 'Tinyhouse'), ('WALK', 'Walk')], default='BOAT', max_length=9, verbose_name='Vehicle Type'),
        ),
    ]
