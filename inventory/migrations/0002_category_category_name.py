# Generated by Django 4.2.3 on 2023-07-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, default='Tools', max_length=100),
        ),
    ]
