# Generated by Django 3.0.3 on 2020-03-10 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0003_model'),
        ('data_handler', '0018_article_smarter_negative_words'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=2000)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_handler.Article')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentiment.Model')),
            ],
        ),
    ]