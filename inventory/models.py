from django.db import models

categories = [('CC', 'Choose Category'),('TLS', 'Tools'), ('PT', 'Paint'), ('TP', 'Tape'), ('WR', 'Wire'), ('FA', 'First Aid'), ('FAB', 'Fabric'), ('PM', 'Paper Mache'), ('GL', 'Glue'), ('SE', 'Sewing'), ('MISC', 'Miscellaneous'), ('CM', 'Coloring Materials'), ('SC', 'Sculpture'), ('WD', 'Wood'), ('CS', 'Craft Supplies'), ('FM', 'Foam'), ('PRTM', 'Printmaking'), ('PAP', 'Paper'), ('DR', 'Drawing')]
vendors = [('CV', 'Choose Vendor'),('DOE', 'ShopDOE'), ('AMZ', 'Amazon'), ('BLICK', 'Blick'), ('HD', 'Home Depot')]
locations = [('CL', 'Choose Location'),('MS', 'Makerspace'), ('BR', 'Back Room')]

class Item(models.Model):
    """ item_id = models.CharField(max_length=100, blank=True, default='') """
    name = models.CharField(max_length=100, blank=True, default="")
    purchase_link = models.CharField(max_length=1000, blank=True, default="")
    """ might want to change to image field """
    image = models.CharField(max_length=1000, blank=True, default="") 
    """ ^^^ """
    last_purchased = models.DateTimeField(auto_now=True, editable=True)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=categories, default="")
    vendor = models.CharField(max_length=50, choices=vendors, default="")
    location = models.CharField(max_length=50, choices=locations, default="")

    def __str__(self):
        return self.name



