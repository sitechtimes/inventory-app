from django.shortcuts import render
from rest_framework import mixins, generics
from django.http import JsonResponse
from rest_framework.response import Response
from django.db.models import Count
from .models import Item, Category
from .serializer import ItemSerializer, CategorySerializer
import datetime
from rest_framework.views import APIView


class AllView(APIView):
    def get(self, request, *args, **kwargs):
        allCategories = Category.objects.all()
        serializer = CategorySerializer(allCategories, many=True)
        return Response(serializer.data)


class sortByCategory(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        queryset = Item.objects.filter(category=category_name)
        return queryset


class categoryCount(generics.ListAPIView):
    queryset = Item.objects.values(
        'category').annotate(count=Count('category'))
    serializer_class = CategorySerializer

    def get_list(self, request, *args, **kwargs):
        """ categories_with_counts = self.get_queryset()
        serialized_data = self.get_serializer(
            categories_with_counts, many=True).data """
        return self.list(request, *args, **kwargs)


class getItems(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.filter(item_id=self.kwargs["item_name"])
        return queryset


class moveItems(generics.UpdateAPIView):
    serializer_class = ItemSerializer

    def get_object(self, obj_id):
        return Item.objects.get(item_id=obj_id)

    def update(self, request, *args, **kwargs):
        item_name = self.kwargs["item_name"]
        fromspace = self.kwargs["from"]
        amount = self.kwargs["amount"]

        obj = self.get_object(item_name)

        if fromspace == 'makerspace_quantity':
            if obj.makerspace_quantity < 0:
                return JsonResponse({"error": "Item is out of stock"}, status=400)
            else:
                if fromspace == 'makerspace_quantity':
                    obj.makerspace_quantity -= amount
                    obj.save()
                    obj.backroom_quantity += amount
                    obj.save()
                else:
                    obj.backroom_quantity -= amount
                    obj.save()
                    obj.makerspace_quantity += amount
                    obj.save()
                return JsonResponse(self.get_serializer(obj).data)
        elif fromspace == 'backroom_quantity':
            if obj.backroom_quantity < 0:
                return JsonResponse({"error": "Item is out of stock"}, status=400)
            else:
                if fromspace == 'makerspace_quantity':
                    obj.makerspace_quantity -= amount
                    obj.save()
                    obj.backroom_quantity += amount
                    obj.save()
                else:
                    obj.backroom_quantity -= amount
                    obj.save()
                    obj.makerspace_quantity += amount
                    obj.save()
                return JsonResponse(self.get_serializer(obj).data)


class UpdateItem(generics.UpdateAPIView):
    serializer_class = ItemSerializer

    def get_object(self, obj_id):
        return Item.objects.get(item_id=obj_id)

    def update(self, *args, **kwargs):
        makerspace_amount = self.kwargs["makerspace"]
        backroom_amount = self.kwargs["backroom"]
        """ queryset = Item.objects.filter(item_id=self.kwargs["item_name"]) """

        obj = self.get_object(self.kwargs["item_name"])
        obj.makerspace_quantity = makerspace_amount
        obj.save()
        obj.backroom_quantity = backroom_amount
        obj.save()

        return JsonResponse(self.get_serializer(obj).data)


class UpdateLastPurchase(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        item.last_purchase = datetime.datetime.now()
        item.save()
        return JsonResponse(self.get_serializer(item).data)
