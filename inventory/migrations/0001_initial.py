# Generated by Django 4.2.3 on 2023-07-20 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('TLS', 'Tools'), ('PT', 'Paint'), ('TP', 'Tape'), ('WR', 'Wire'), ('FA', 'First Aid'), ('FAB', 'Fabric'), ('PM', 'Paper Mache'), ('GL', 'Glue'), ('SE', 'Sewing'), ('MISC', 'Miscellaneous'), ('CM', 'Coloring Materials'), ('SC', 'Sculpture'), ('WD', 'Wood'), ('CS', 'Craft Supplies'), ('FM', 'Foam'), ('PRTM', 'Printmaking'), ('PAP', 'Paper'), ('DR', 'Drawing')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(blank=True, default='', max_length=100)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('purchase_link', models.CharField(blank=True, default='', max_length=1000)),
                ('image', models.CharField(blank=True, default='', max_length=1000)),
                ('last_purchased', models.DateTimeField(auto_now=True)),
                ('backroom_quantity', models.IntegerField(default=0)),
                ('makerspace_quantity', models.IntegerField(default=0)),
                ('vendor', models.CharField(choices=[('DOE', 'ShopDOE'), ('AMZ', 'Amazon'), ('BLICK', 'Blick'), ('HD', 'Home Depot')], default='', max_length=50)),
                ('location', models.CharField(choices=[('MS', 'Makerspace'), ('BR', 'Back Room')], default='', max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.category')),
            ],
        ),
    ]
