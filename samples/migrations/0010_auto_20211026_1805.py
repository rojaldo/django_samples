# Generated by Django 3.2.8 on 2021-10-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0009_mytrivialcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytrivialcard',
            name='incorrect_answers_2',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='mytrivialcard',
            name='incorrect_answers_3',
            field=models.CharField(default='', max_length=120),
        ),
    ]