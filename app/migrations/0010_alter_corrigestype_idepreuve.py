# Generated by Django 3.2.3 on 2021-06-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210616_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corrigestype',
            name='idEpreuve',
            field=models.CharField(max_length=100),
        ),
    ]