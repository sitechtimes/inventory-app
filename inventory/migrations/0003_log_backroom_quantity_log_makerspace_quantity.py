# Generated by Django 4.2.5 on 2023-09-30 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='backroom_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='log',
            name='makerspace_quantity',
            field=models.IntegerField(default=0),
        ),
    ]