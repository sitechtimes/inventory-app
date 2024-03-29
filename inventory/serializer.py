from rest_framework import serializers
from .models import Item, Category, Vendor, Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['name', 'backroom_quantity', 'makerspace_quantity',
                  'purchase_link', 'pub_date', 'category', 'vendor', 'dateTime', 'change']


class ItemSerializer(serializers.ModelSerializer):

    total = serializers.SerializerMethodField()

    image = serializers.ImageField(required=False)
    url = serializers.URLField(required=False, allow_blank=True)

    alert = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ItemSerializer, self).to_representation(instance)
        rep['category'] = instance.category.category_name
        rep['vendor'] = instance.vendor.vendor_name
        return rep

    def get_total(self, obj):
        total = obj.backroom_quantity + obj.makerspace_quantity
        return total

    def get_alert(self, obj):
        total = obj.backroom_quantity + obj.makerspace_quantity

        if total > obj.min_amount:
            alert = False

        else:
            alert = True

        return alert


class CategorySerializer(serializers.ModelSerializer):
    itemsCategory = ItemSerializer(many=True)
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'category_name', "category_code",
                  'itemsCategory', 'count')

    def get_count(self, obj):
        count = Item.objects.filter(category=obj).count()
        return count


class VendorSerializer(serializers.ModelSerializer):
    itemsVendor = ItemSerializer(many=True)
    count = serializers.SerializerMethodField()

    class Meta:
        model = Vendor
        fields = ('vendor_name', 'vendor_code', 'itemsVendor', 'count')

    def get_count(self, obj):
        count = Item.objects.filter(vendor=obj).count()
        return count
