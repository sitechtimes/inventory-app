from django.shortcuts import render
from rest_framework import mixins, generics
from django.http import JsonResponse
from .models import Item
from .serializer import ItemSerializer
import datetime

class ItemsView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class category_list(generics.ListAPIView): 
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        queryset = Item.objects.filter(category=category_name)
        return queryset

class MakerspaceView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.filter(location="Makerspace")
        return queryset

class BackroomView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.filter(location="Back Room")
        return queryset

class getItems(generics.ListAPIView):
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        queryset = Item.objects.filter(item_id=self.kwargs["item_name"])
        return queryset

class moveItems(generics.UpdateAPIView):
    serializer_class = ItemSerializer

    def get_object(self, obj_id, obj_location):
        return Item.objects.get(item_id=obj_id, location=obj_location)
    
    def update(self, request, *args, **kwargs): 
        item_name = self.kwargs["item_name"]
        fromspace = self.kwargs["from"]
        tospace = self.kwargs["to"]
        amount = self.kwargs["amount"]
        

        obj = self.get_object(item_name, fromspace)
        obj2 = self.get_object(item_name, tospace)

        if obj.quantity == 0:
            return JsonResponse({"error": "Item is out of stock"}, status=400)
        else: 
            obj.quantity -= amount 
            obj.save()
            obj2.quantity += amount
            obj2.save()
            return JsonResponse(self.get_serializer(obj2).data)

class UpdateItem(generics.UpdateAPIView):
    serializer_class = ItemSerializer

    def update(self, *args, **kwargs): 
        makerspace_amount = self.kwargs["makerspace"]
        backroom_amount = self.kwargs["backroom"]
        queryset = Item.objects.filter(item_id=self.kwargs["item_name"])

        obj = queryset.get(location="Makerspace")
        obj2 = queryset.get(location="Back Room")
        obj.quantity = makerspace_amount
        obj.save()
        obj2.quantity = backroom_amount
        obj2.save()
    

        return JsonResponse(self.get_serializer(obj).data)
    

class UpdateLastPurchase(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        item.last_purchase = datetime.datetime.now()
        item.save()
        return JsonResponse(self.get_serializer(item).data)