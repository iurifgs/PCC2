# Generated by Django 4.2.6 on 2024-05-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_alter_animal_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='data_nascimento',
            field=models.DateField(default='2024-05-29'),
        ),
    ]