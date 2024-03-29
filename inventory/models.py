from django.db import models
from django.utils import timezone
import datetime

categories = [('TLS', 'Tools'), ('PT', 'Paint'), ('TP', 'Tape'), ('WR', 'Wire'), ('FA', 'First Aid'), ('FAB', 'Fabric'), ('PM', 'Paper Mache'), ('GL', 'Glue'), ('SE', 'Sewing'), ('MISC','Miscellaneous'), ('CM', 'Coloring Materials'), ('SC', 'Sculpture'), ('WD', 'Wood'), ('CS', 'Craft Supplies'), ('FM', 'Foam'), ('PRTM', 'Printmaking'), ('PAP', 'Paper'), ('DR', 'Drawing'), ('RES', 'Resin Printer'), ('3D', '3D Printer'), ('STGL', 'Stained Glass')]


vendors = [('DOE', 'ShopDOE'), ('AMZ', 'Amazon'), ('BLICK', 'Blick'), ('HD', 'Home Depot'),('Fl' , 'Form Labs'),('BL' , 'Bambu Lab'),('HL' , 'Hobby Lobby'),('FAST' , 'Fastenal'),('GLCRFT' , 'Glass Crafters'),('MIC' , 'Michaels'),('ADO' , 'Adorama')]
locations = [('MS', 'Makerspace'), ('BR', 'Back Room')]

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()
class Category(models.Model):
    category_code = models.CharField(
        choices=categories, max_length=100, default="")
    category_name = models.CharField(
        choices=categories, max_length=100, default="")

    def __str__(self):
        return self.category_name


class Vendor(models.Model):
    vendor_code = models.CharField(
        choices=vendors, max_length=100, default=None)
    vendor_name = models.CharField(
        choices=vendors, max_length=100, default=None)

    def __str__(self):
        return self.vendor_name


def upload_to(instance, filename):
    count_obj = Item.objects.all().count() + 1
    return 'images/{count}/{filename}'.format(count=count_obj, filename=filename)


class Item(models.Model):
    item_id = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    purchase_link = models.CharField(max_length=1000, blank=True, default='')
    image_url = models.URLField(blank=True, null=True, default=None)
    image_file = models.ImageField(
        upload_to=upload_to, blank=True, null=True, default=None)
    last_purchased = models.DateTimeField(auto_now=True, editable=True)
    backroom_quantity = models.IntegerField(default=0)
    makerspace_quantity = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, related_name='itemsCategory', on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        Vendor, related_name='itemsVendor', on_delete=models.CASCADE)
    location = models.CharField(max_length=50, default='')
    min_amount = models.IntegerField(default=5)

    def __str__(self):
        return self.name

    # this may conflict with stuff idk
    def delete(self, *args, **kwargs):
        count_obj = Item.objects.all().count() + 1
        self.id = count_obj
        super(Item, self).save(*args, **kwargs)


class Log(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    dateTime = models.DateTimeField(default=timezone.now)
    category = models.CharField(
        max_length=50, choices=categories, default='TLS')
    purchase_link = models.CharField(max_length=1000, blank=True, default='')
    backroom_quantity = models.IntegerField(default=0)
    makerspace_quantity = models.IntegerField(default=0)
    vendor = models.CharField(max_length=50, choices=vendors, default='DOE')
    pub_date = models.CharField(
        max_length=100, blank=True, default='00/00/0000')
    change = models.CharField(max_length=2000, blank=False, default='')

    def __str__(self):
        return self.name
# image = models.CharField(max_length=1000, blank=True, default='')...
