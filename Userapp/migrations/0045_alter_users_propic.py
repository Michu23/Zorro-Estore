# Generated by Django 4.0.2 on 2022-03-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0044_alter_users_propic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='propic',
            field=models.ImageField(blank=True, default='/images/DP22.png', null=True, upload_to='images'),
        ),
    ]
