# Generated by Django 4.2.3 on 2023-07-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, max_length=14),
        ),
    ]