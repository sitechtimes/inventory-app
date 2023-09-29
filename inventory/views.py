import statistics
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from django.http import JsonResponse, Http404
from rest_framework.response import Response
from .models import Item, Category, Vendor, Log
from .serializer import ItemSerializer, CategorySerializer, VendorSerializer, LogSerializer
import datetime
from rest_framework.parsers import MultiPartParser, FormParser

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


class sortByVendor(generics.ListAPIView):
    serializer_class = VendorSerializer

    def get_queryset(self):
        vendor_name = self.kwargs["vendor_name"]
        queryset = Vendor.objects.filter(vendor_name=vendor_name)
        return queryset


class UpdateLastPurchase(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        item.last_purchased = datetime.datetime.now()
        item.save()
        return JsonResponse(self.get_serializer(item).data)


class getItems(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


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


class AddItems(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # def create(self, request, *args, **kwargs):
    #     # image_file = request.FILES.get('image_file')
    #     # if image_file is None:
    #     #     return Response({'message': 'Image file is required.'}, status=400)

    #     # Create a new serializer instance with only the image file data
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # Save the image file separately, perform_create method can be used
    #     # to handle further creation logic if needed
    #     self.perform_create(serializer)

    #     return Response(serializer.data, status=201)

# delete item by pk value (id)


class deleteItems(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()

        return Response("Item deleted", status=204)


class updateMinAmount(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        itemMinAmount = self.get_object()

        amount = self.kwargs["amount"]

        itemMinAmount.min_amount = amount

        itemMinAmount.save()

        return Response("Item updated", status=200)


class editItems(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
