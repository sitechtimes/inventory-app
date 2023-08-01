from django.conf import settings
import os
import django
import pandas as pd
from inventory.models import Item
from inventory.models import Category
from inventory.models import Vendor
from django.core.files import File


def run():
    dataframe = pd.read_csv('scripts/csv/inventory - inventory.csv')

    Item.objects.all().delete()
    Category.objects.all().delete()
    Vendor.objects.all().delete()
    print('Hello world!')

    for index, rows in dataframe.iterrows():
        try:
            Category.objects.get(category_name=rows["Category"])
        except Category.DoesNotExist:
            category_name = Category(category_name=rows["Category"])
            category_name.save()

        try:
            Vendor.objects.get(vendor_name=rows["Vendor"])
        except Vendor.DoesNotExist:
            vendor_name = Vendor(vendor_name=rows["Vendor"])
            vendor_name.save()

        try:
            image_path = rows["Image"] if pd.notnull(rows["Image"]) else None
            print(image_path)
            item = Item(
                item_id=rows["Item ID"],
                name=rows["Name"],
                purchase_link=rows["Purchase Link"],
                image=image_path,
                last_purchased=rows["Date Last Purchased"],
                backroom_quantity=rows["Backroom_quantity"],
                makerspace_quantity=rows["Makerspace_quantity"],
                category=Category.objects.get(category_name=rows["Category"]),
                vendor=Vendor.objects.get(vendor_name=rows["Vendor"]),
                location=rows["Location"],
                min_amount=rows["Alert"]
            )
            item.save()
        except Exception as e:
            print(f"Error adding item: {e}")

    print("Successfully added items from CSV to inventory.")
