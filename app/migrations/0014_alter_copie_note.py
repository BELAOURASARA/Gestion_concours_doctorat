# Generated by Django 3.2.3 on 2021-06-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_copie_isvalidated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copie',
            name='note',
            field=models.IntegerField(null=True),
        ),
    ]
