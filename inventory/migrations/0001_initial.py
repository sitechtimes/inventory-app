# Generated by Django 4.2.3 on 2023-08-03 12:28

from django.db import migrations, models
import django.db.models.deletion
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(choices=[('TLS', 'Tools'), ('PT', 'Paint'), ('TP', 'Tape'), ('WR', 'Wire'), ('FA', 'First Aid'), ('FAB', 'Fabric'), ('PM', 'Paper Mache'), ('GL', 'Glue'), ('SE', 'Sewing'), ('MISC', 'Miscellaneous'), ('CM', 'Coloring Materials'), ('SC', 'Sculpture'), ('WD', 'Wood'), ('CS', 'Craft Supplies'), ('FM', 'Foam'), ('PRTM', 'Printmaking'), ('PAP', 'Paper'), ('DR', 'Drawing')], default='', max_length=100)),
                ('category_name', models.CharField(choices=[('TLS', 'Tools'), ('PT', 'Paint'), ('TP', 'Tape'), ('WR', 'Wire'), ('FA', 'First Aid'), ('FAB', 'Fabric'), ('PM', 'Paper Mache'), ('GL', 'Glue'), ('SE', 'Sewing'), ('MISC', 'Miscellaneous'), ('CM', 'Coloring Materials'), ('SC', 'Sculpture'), ('WD', 'Wood'), ('CS', 'Craft Supplies'), ('FM', 'Foam'), ('PRTM', 'Printmaking'), ('PAP', 'Paper'), ('DR', 'Drawing')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(choices=[('DOE', 'ShopDOE'), ('AMZ', 'Amazon'), ('BLICK', 'Blick'), ('HD', 'Home Depot')], default=None, max_length=100)),
                ('vendor_name', models.CharField(choices=[('DOE', 'ShopDOE'), ('AMZ', 'Amazon'), ('BLICK', 'Blick'), ('HD', 'Home Depot')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(blank=True, default='', max_length=100)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('purchase_link', models.CharField(blank=True, default='', max_length=1000)),
                ('image_url', models.URLField(blank=True, default=None, null=True)),
                ('image_file', models.ImageField(blank=True, default=None, null=True, upload_to=inventory.models.upload_to)),
                ('last_purchased', models.DateTimeField(auto_now=True)),
                ('backroom_quantity', models.IntegerField(default=0)),
                ('makerspace_quantity', models.IntegerField(default=0)),
                ('location', models.CharField(default='', max_length=50)),
                ('min_amount', models.IntegerField(default=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemsCategory', to='inventory.category')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemsVendor', to='inventory.vendor')),
            ],
        ),
    ]
