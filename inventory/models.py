from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

categories = [('TLS', 'Tools'), ('PT', 'Paint'), ('TP', 'Tape'), ('WR', 'Wire'), ('FA', 'First Aid'), ('FAB', 'Fabric'), ('PM', 'Paper Mache'), ('GL', 'Glue'), ('SE', 'Sewing'), ('MISC',
                                                                                                                                                                                   'Miscellaneous'), ('CM', 'Coloring Materials'), ('SC', 'Sculpture'), ('WD', 'Wood'), ('CS', 'Craft Supplies'), ('FM', 'Foam'), ('PRTM', 'Printmaking'), ('PAP', 'Paper'), ('DR', 'Drawing')]


vendors = [('DOE', 'ShopDOE'), ('AMZ', 'Amazon'),
           ('BLICK', 'Blick'), ('HD', 'Home Depot')]
locations = [('MS', 'Makerspace'), ('BR', 'Back Room')]


class Category(models.Model):
    category_name = models.CharField(choices=categories, max_length=100)

    def __str__(self):
        return self.category_name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE)
    item_id = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    purchase_link = models.CharField(max_length=1000, blank=True, default='')
    image = models.CharField(max_length=1000, blank=True, default='')
    last_purchased = models.DateTimeField(auto_now=True, editable=True)
    backroom_quantity = models.IntegerField(default=0)
    makerspace_quantity = models.IntegerField(default=0)
    vendor = models.CharField(max_length=50, choices=vendors, default='')
    location = models.CharField(max_length=50, choices=locations, default='')

    def __str__(self):
        return self.name
