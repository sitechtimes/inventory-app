# Generated by Django 4.2.5 on 2023-09-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_log_category_log_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='pub_date',
            field=models.CharField(blank=True, default='00/00/0000', max_length=100),
        ),
    ]
