from django.contrib import admin
from .models import Item, Category, Vendor, Log

admin.site.register([Item, Category, Vendor, Log])
