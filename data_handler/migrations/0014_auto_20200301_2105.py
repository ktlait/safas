# Generated by Django 3.0.3 on 2020-03-01 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0013_auto_20200301_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]