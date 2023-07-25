import django
import pandas as pd
from inventory.models import Item
from inventory.models import Category
from inventory.models import Vendor


def run():
    dataframe = pd.read_csv('scripts/csv/inventory.csv')

    Item.objects.all().delete()
    Category.objects.all().delete()
    Vendor.objects.all().delete()
    print('Hello world!')
    for index, rows in dataframe.iterrows():
        try:
            Category.objects.get(category_name=rows["Category"])

        except:
            category_name = Category(category_name=rows["Category"])
            category_name.save()

        try:
            Vendor.objects.get(vendor_name=rows["Vendor"])
        except:
            vendor_name = Vendor(vendor_name=rows["Vendor"])
            vendor_name.save()
        try:
            item = Item(
                item_id=rows[" Item ID"],
                name=rows["Name"],
                purchase_link=rows["Purchase Link"],
                image=rows["Image"],
                last_purchased=rows["Date Last Purchased"],
                backroom_quantity=2,
                makerspace_quantity=2,
                category=Category.objects.get(category_name=rows["Category"]),
                vendor=Vendor.objects.get(vendor_name=rows["Vendor"]),
                location="Makerspace",
                suppliesNeeded=False,
            )
            item.save()
        except django.db.utils.IntegrityError:
            pass
    print("Successfully added items from csv to inventory.")
