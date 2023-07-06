# Generated by Django 4.2.3 on 2023-07-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_delete_categories_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('HARDWARE', 'Hardware'), ('ART SUPPLIES', 'Art Supplies'), ('OTHER', 'Other')], default='', max_length=50),
        ),
    ]
