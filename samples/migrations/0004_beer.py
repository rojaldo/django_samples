# Generated by Django 3.2.8 on 2021-10-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0003_nasaapod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_id', models.IntegerField()),
                ('name', models.CharField(max_length=120)),
                ('tagline', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('abv', models.FloatField()),
                ('first_brewed', models.DateField()),
                ('image_url', models.URLField(max_length=100)),
            ],
        ),
    ]
