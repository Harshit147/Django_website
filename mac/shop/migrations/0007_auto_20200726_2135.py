# Generated by Django 3.0.6 on 2020-07-26 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Order_Id',
            new_name='order_id',
        ),
    ]
