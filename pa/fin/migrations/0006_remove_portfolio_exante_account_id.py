# Generated by Django 3.1.9 on 2021-06-14 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0005_stockexchange_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='exante_account_id',
        ),
    ]
