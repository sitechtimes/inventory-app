from django.shortcuts import render
from rest_framework import mixins, generics
from django.http import JsonResponse
from .models import Item
from .serializer import ItemSerializer

class ItemsView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class category_list(generics.ListAPIView): 
    serializer_class = ItemSerializer
    

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        queryset = Item.objects.filter(category__name=category_name)
        return queryset
    
