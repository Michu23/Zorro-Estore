# Generated by Django 4.0.2 on 2022-02-16 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0005_remove_address_date_added_address_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='semester',
            new_name='type',
        ),
    ]
