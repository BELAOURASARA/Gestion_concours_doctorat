# Generated by Django 3.2.3 on 2021-06-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_copie_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copie',
            name='subi3eme',
            field=models.BooleanField(null=True),
        ),
    ]
