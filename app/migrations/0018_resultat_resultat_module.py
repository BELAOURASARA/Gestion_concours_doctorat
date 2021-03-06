# Generated by Django 3.2.3 on 2021-06-18 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210618_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultat_module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ep', models.CharField(max_length=100)),
                ('moy_note', models.IntegerField()),
                ('matricule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidat')),
            ],
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resul', models.IntegerField()),
                ('matricule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidat')),
            ],
        ),
    ]
