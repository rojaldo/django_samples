# Generated by Django 3.2.8 on 2021-10-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='NasaAPOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.CharField(default='unknown', max_length=50)),
                ('date', models.DateField()),
                ('explanation', models.TextField()),
                ('hdurl', models.URLField(default='', max_length=100)),
                ('media_type', models.CharField(max_length=10)),
                ('service_version', models.CharField(max_length=2)),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=100)),
            ],
        ),
    ]
