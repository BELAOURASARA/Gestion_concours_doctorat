# Generated by Django 3.2.3 on 2021-06-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210615_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='exclu',
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name='Copie',
        ),
    ]