# Generated by Django 3.1.2 on 2020-10-23 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kegiatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Orang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orang', models.CharField(max_length=150)),
                ('kegiatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kegiatan.kegiatan')),
            ],
        ),
    ]
