# Generated by Django 4.0.2 on 2022-02-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0009_alter_orderitem_order_alter_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='New', max_length=200, null=True),
        ),
    ]
