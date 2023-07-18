from rest_framework import serializers
from .models import Item, Categories

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta: 
        model = Categories
        fields = ('category_name', 'count')
    
    def get_count(self, obj):
        count = Item.objects.filter(category__in=[obj]).count()
        return count
   