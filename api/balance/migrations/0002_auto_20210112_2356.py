# Generated by Django 3.1.3 on 2021-01-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='total_money',
            field=models.FloatField(default=0.0),
        ),
    ]