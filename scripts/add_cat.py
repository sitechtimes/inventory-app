import django 
import pandas as pd
from inventory.models import Categories

def add_categories():
    df = pd.read_csv('category.csv')
    categories_data = df.to_dict(orient='records')

    for category_data in categories_data:
        try:
            Categories.objects.get_or_create(
            category_code=category_data['category_code'],
            category_name=category_data['category_name']
        )
            
        except django.db.utils.IntegrityError:
            pass
 
    print(f"Category '{category_data['category_name']}' added.")