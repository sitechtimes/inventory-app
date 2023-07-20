from rest_framework import generics
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Item, Category, Vendor
from .serializer import ItemSerializer, CategorySerializer, VendorSerializer
import datetime
from rest_framework.views import APIView


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VendorView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class sortByCategory(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        queryset = Category.objects.filter(category_name=category_name)
        return queryset


class UpdateLastPurchase(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        item.last_purchased = datetime.datetime.now()
        item.save()
        return JsonResponse(self.get_serializer(item).data)


class getItems(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.filter(id=self.kwargs["pk"])
        return queryset


class moveItems(generics.UpdateAPIView):
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        queryset = Item.objects.get(id=self.kwargs["pk"])
        itemfrom = self.kwargs['from']

        if itemfrom == 'backroom':
            if queryset.backroom_quantity == 0:
                return JsonResponse({'error': 'Item is out of stock in BackRoom'}, status=400)
            else:
                queryset.backroom_quantity -= 1
                queryset.makerspace_quantity += 1
                queryset.save()

                return JsonResponse(self.get_serializer(queryset).data)
        if itemfrom == 'makerspace':
            if queryset.makerspace_quantity == 0:
                return JsonResponse({'error': 'Item is out of stock in MakerSpace'}, status=400)
            else:
                queryset.makerspace_quantity -= 1
                queryset.backroom_quantity += 1
                queryset.save()

                return JsonResponse(self.get_serializer(queryset).data)


class ManualEditQuantity(generics.UpdateAPIView):
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        queryset = Item.objects.get(id=self.kwargs["pk"])
        makerspace = self.kwargs["makerspace"]
        backroom = self.kwargs["backroom"]
        if makerspace >= 0 and backroom >= 0:
            queryset.makerspace_quantity = makerspace
            queryset.backroom_quantity = backroom
            queryset.save()

            return JsonResponse(self.serializer_class(queryset).data)
        else:
            return JsonResponse({'error': 'Invalid input'}, status=400)
