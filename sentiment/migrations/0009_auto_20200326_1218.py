# Generated by Django 3.0.3 on 2020-03-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0008_label_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='model_name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]