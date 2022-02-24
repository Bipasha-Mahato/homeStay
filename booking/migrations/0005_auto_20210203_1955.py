# Generated by Django 3.1.2 on 2021-02-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20201117_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='currency',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='receipt',
            field=models.CharField(default=False, max_length=10),
        ),
    ]