# Generated by Django 3.0.6 on 2020-07-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('Order_Id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=110)),
                ('city', models.CharField(max_length=110)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
    ]
