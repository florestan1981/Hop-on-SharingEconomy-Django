# Generated by Django 3.1.7 on 2021-08-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0014_auto_20210823_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='auctionImage',
            field=models.ImageField(default='default_auction.png', upload_to='', verbose_name='Auction Image'),
        ),
    ]
