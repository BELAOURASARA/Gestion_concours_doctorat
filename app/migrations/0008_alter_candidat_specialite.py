# Generated by Django 3.2.3 on 2021-06-15 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210615_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='specialite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.specialite'),
        ),
    ]