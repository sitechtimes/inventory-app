from rest_framework import serializers
from .models import Item, Category
from django.db.models import Count

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('title', 'posts')

    def get_posts(self,obj):
        posts = Item.objects.values('category').annotate(count=Count('category')).filter(category=obj)
        return posts
