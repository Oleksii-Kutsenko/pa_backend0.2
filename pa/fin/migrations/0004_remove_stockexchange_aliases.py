# Generated by Django 3.1.9 on 2021-06-08 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0003_auto_20210608_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockexchange',
            name='aliases',
        ),
    ]
