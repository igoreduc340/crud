# Generated by Django 4.2.11 on 2024-04-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='idade',
            field=models.IntegerField(max_length=3),
        ),
    ]