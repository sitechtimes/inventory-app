import django
import pandas as pd
from inventory.models import Item

def run():
    dataframe = pd.read_csv('scripts/csv/inventory.csv')
    print(dataframe["Category"])
    print(Item.objects.all())

    for index, rows in dataframe.iterrows():
        try:

            item = Item(
                item_id=rows[" Item ID"],
                name=rows["Name"],
                purchase_link=rows["Purchase Link"],
                image=rows["Image"],
                last_purchased=rows["Date Last Purchased"],
                quantity=2,
                category=rows["Category"],
                vendor=rows["Vendor"],
                location="Back Room"
            )
            item.save()
        except django.db.utils.IntegrityError:
            pass
    print("Successfully added items from csv to inventory.")
