# Generated by Django 3.1.2 on 2020-11-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='address',
            field=models.CharField(default=0, max_length=400),
            preserve_default=False,
        ),
    ]