# Generated by Django 3.0.3 on 2020-03-01 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0012_stockprice_interday_volatility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='volume',
            field=models.BigIntegerField(),
        ),
    ]