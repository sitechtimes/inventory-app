from django.conf import settings
import os
import django
import pandas as pd
from inventory.models import Item
from inventory.models import Category
from inventory.models import Vendor

categories = [('TLS', 'Tools'), ('PT', 'Paint'), ('TP', 'Tape'), ('WR', 'Wire'), ('FA', 'First Aid'), ('FAB', 'Fabric'), ('PM', 'Paper Mache'), ('GL', 'Glue'), ('SE', 'Sewing'), ('MISC',
                                                                                                                                                                                   'Miscellaneous'), ('CM', 'Coloring Materials'), ('SC', 'Sculpture'), ('WD', 'Wood'), ('CS', 'Craft Supplies'), ('FM', 'Foam'), ('PRTM', 'Printmaking'), ('PAP', 'Paper'), ('DR', 'Drawing')]


vendors = [('DOE', 'ShopDOE'), ('AMZ', 'Amazon'),
           ('BLICK', 'Blick'), ('HD', 'Home Depot')]


def run():
    dataframe = pd.read_csv('scripts/csv/inventory.csv')

    Item.objects.all().delete()
    Category.objects.all().delete()
    Vendor.objects.all().delete()
    print('Creating Items')

    try:
        for code, name in categories:
            category = Category(
                category_code=code,
                category_name=name,
            )
            category.save()
    except:
        print(f"The category '{name}' failed.")
    try:
        for code, name in vendors:
            vendor = Vendor(
                vendor_code=code,
                vendor_name=name
            )
            vendor.save()
    except:
        print(f"The Vendor '{name}' failed.")
    for index, rows in dataframe.iterrows():
        try:
            image_path = rows["Image_file"] if pd.notnull(
                rows["Image_file"]) else None
            item_vendor = Vendor.objects.get(
                vendor_code=rows["vendor_code"]) if pd.notnull(rows["vendor_code"]) else None
            item = Item(
                item_id=rows["Item ID"],
                name=rows["Name"],
                purchase_link=rows["Purchase Link"],
                image_url=rows["Image_url"],
                image_file=image_path,
                last_purchased=rows["Date Last Purchased"],
                backroom_quantity=rows["Backroom_quantity"],
                makerspace_quantity=rows["Makerspace_quantity"],
                category=Category.objects.get(
                    category_code=rows["category_code"]),
                vendor=item_vendor,
                location=rows["Location"],
                min_amount=rows["Alert"],
            )
            item.save()
            """ except Exception as e:
            print(f"Error adding item: {e}") """

        except django.db.utils.IntegrityError:
            pass
    print("Successfully added items from CSV to inventory.")


"""         try:
            Category.objects.get(category_name=rows["Category"])
        except Category.DoesNotExist:
            category_name = Category(category_name=rows["Category"])
            category_name.save()

        try:
            Vendor.objects.get(vendor_name=rows["Vendor"])
        except Vendor.DoesNotExist:
            vendor_name = Vendor(vendor_name=rows["Vendor"])
            vendor_name.save() """
