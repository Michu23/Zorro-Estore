# Generated by Django 4.0.2 on 2022-02-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0021_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
