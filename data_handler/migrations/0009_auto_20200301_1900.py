# Generated by Django 3.0.3 on 2020-03-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0008_auto_20200228_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_written',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]