# Generated by Django 3.1.7 on 2021-08-17 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='v_description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_name',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.IntegerField()),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('createdDAte', models.DateTimeField(auto_now_add=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.vehicle')),
            ],
        ),
    ]
