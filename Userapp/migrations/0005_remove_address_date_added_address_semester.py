# Generated by Django 4.0.2 on 2022-02-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0004_remove_address_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='date_added',
        ),
        migrations.AddField(
            model_name='address',
            name='semester',
            field=models.CharField(choices=[('1', 'Home'), ('2', 'Work')], default='1', max_length=20),
        ),
    ]
