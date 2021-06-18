# Generated by Django 3.2.3 on 2021-06-18 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_merge_0013_fichiers_0015_alter_copie_subi3eme'),
    ]

    operations = [
        migrations.CreateModel(
            name='table_inter_correction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(max_length=100)),
                ('note', models.IntegerField(null=True)),
                ('id_copie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.copie')),
                ('id_correcteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.correcteur')),
            ],
        ),
        migrations.DeleteModel(
            name='table_inter',
        ),
    ]
