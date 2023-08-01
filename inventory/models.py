from django.db import models

categories = [('TLS', 'Tools'), ('PT', 'Paint'), ('TP', 'Tape'), ('WR', 'Wire'), ('FA', 'First Aid'), ('FAB', 'Fabric'), ('PM', 'Paper Mache'), ('GL', 'Glue'), ('SE', 'Sewing'), ('MISC',
                                                                                                                                                                                   'Miscellaneous'), ('CM', 'Coloring Materials'), ('SC', 'Sculpture'), ('WD', 'Wood'), ('CS', 'Craft Supplies'), ('FM', 'Foam'), ('PRTM', 'Printmaking'), ('PAP', 'Paper'), ('DR', 'Drawing')]


vendors = [('DOE', 'ShopDOE'), ('AMZ', 'Amazon'),
           ('BLICK', 'Blick'), ('HD', 'Home Depot')]
locations = [('MS', 'Makerspace'), ('BR', 'Back Room')]


class Category(models.Model):
    category_name = models.CharField(choices=categories, max_length=100)

    def __str__(self):
        return self.category_name


class Vendor(models.Model):
    vendor_name = models.CharField(choices=vendors, max_length=100)

    def __str__(self):
        return self.vendor_name


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


"""  min_amount = models.IntegerField(default=0) """


class Item(models.Model):
    item_id = models.CharField(max_length=100, blank=False, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    purchase_link = models.CharField(max_length=1000, blank=True, default='')
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    last_purchased = models.DateTimeField(auto_now=True, editable=True)
    backroom_quantity = models.IntegerField(default=0)
    makerspace_quantity = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, related_name='itemsCategory', on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        Vendor, related_name='itemsVendor', on_delete=models.CASCADE)
    location = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        count_obj = Item.objects.all().count()+1
        self.id = count_obj
        super(Item, self).save(*args, **kwargs)

# image = models.CharField(max_length=1000, blank=True, default='')
