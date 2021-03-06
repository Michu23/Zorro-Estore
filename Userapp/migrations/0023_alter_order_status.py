# Generated by Django 4.0.2 on 2022-03-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0022_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Placed', 'Placed'), ('Shipped', 'Shipped'), ('RequestedCancellation', 'RequestedCancellation'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered'), ('RequestedReturn', 'RequestedReturn'), ('Return', 'Return')], default='New', max_length=200, null=True),
        ),
    ]
