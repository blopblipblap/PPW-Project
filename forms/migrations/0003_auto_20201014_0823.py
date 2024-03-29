# Generated by Django 3.1.2 on 2020-10-14 01:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_matkul_dosen'),
    ]

    operations = [
        migrations.AddField(
            model_name='matkul',
            name='deskripsi',
            field=models.TextField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matkul',
            name='kelas',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matkul',
            name='semester',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matkul',
            name='sks',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
