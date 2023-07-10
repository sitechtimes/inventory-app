from django.shortcuts import render
from rest_framework import mixins, generics
from django.http import JsonResponse
from .models import Item
from .serializer import ItemSerializer
""" 
class ItemsView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
     """

class ItemsCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemsList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemsUpdate(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemsDestroy(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer