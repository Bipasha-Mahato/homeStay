# Generated by Django 3.1.2 on 2020-11-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20201117_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(),
        ),
    ]