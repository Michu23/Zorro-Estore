# Generated by Django 4.0.2 on 2022-02-14 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0003_order_orderitem_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
    ]
