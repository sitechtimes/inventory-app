from django.contrib import admin

from .models import Item
from .models import Categories

admin.site.register([Item, Categories])