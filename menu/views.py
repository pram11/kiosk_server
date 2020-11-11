from django.shortcuts import render
from django.http.response import HttpResponseBadRequest
from rest_framework.decorators import api_view
from rest_framework.views import Response, Http404
from rest_framework import generics
from menu.models import MenuCategory,MenuItem
from menu.serializers import MenuCategorySerializer,MenuItemSerializer


class MenuCategoryListView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        category = self.kwargs['category_id']
        return MenuItem.objects.filter(category_id=category)


class ItemListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        queryset = MenuItem.objects.all()
        menu = self.request.query_params.get('menu',None)
        if menu is not None:
            queryset = queryset.filter(name__icontains=menu)
        return queryset
