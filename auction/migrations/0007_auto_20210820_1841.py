# Generated by Django 3.1.7 on 2021-08-20 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_auction_tripdetails'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='bid',
            order_with_respect_to='price',
        ),
    ]
