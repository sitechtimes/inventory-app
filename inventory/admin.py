from django.contrib import admin
from .models import Item, Category, Vendor

admin.site.register([Item, Category, Vendor])
