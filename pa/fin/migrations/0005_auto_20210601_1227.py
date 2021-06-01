# Generated by Django 3.1.8 on 2021-06-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0004_auto_20210601_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.CharField(choices=[('CAD', 'Canadian Dollar'), ('EUR', 'Euro'), ('UAH', 'Ukrainian Hryvnia'), ('USD', 'United States Dollar')], max_length=3),
        ),
    ]
