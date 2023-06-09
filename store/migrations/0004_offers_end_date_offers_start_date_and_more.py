# Generated by Django 4.1.4 on 2023-02-12 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_orders_address_alter_orders_expected_deliverydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='end_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='start_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='dicount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2023, 2, 17)),
        ),
    ]
