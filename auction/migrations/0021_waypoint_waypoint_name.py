# Generated by Django 3.1.7 on 2021-08-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0020_waypoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='waypoint',
            name='waypoint_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
