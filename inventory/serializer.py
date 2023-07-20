from rest_framework import serializers
from .models import Item, Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ('category',)


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('category_name', 'items', 'count')

    def get_count(self, obj):
        count = Item.objects.filter(category=obj).count()
        return count
