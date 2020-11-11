from django.shortcuts import render
from django.http.response import HttpResponseBadRequest,HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.views import Response, Http404
from rest_framework import generics
from order import models
from order import serializers
from menu.models import MenuItem


# Create your views here.

@api_view(['GET', 'POST'])
def orderListView(request):
    if request.method == "GET":
        orders = models.Order.objects.all()
        serializer = serializers.OrderSerializer(instance=orders,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        order = models.Order.objects.create()
        print(order.id)
        return Response({'id':order.id})

@api_view(['GET', 'PUT'])
def orderDetailView(request, order_id):
    try:
        queryset = models.Order.objects.get(id=order_id)
    except models.Order.DoesNotExist:
        raise Http404
    if request.method == "GET":
        serializer = serializers.OrderSerializer(queryset)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = serializers.OrderSerializer(data=request.data)
        if not serializer.is_valid():
            return HttpResponseBadRequest()
        queryset.status = serializer.validated_data['status']
        queryset.save()
        serializer = serializers.OrderSerializer(queryset)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def orderItemListView(request, order_id):
    try:
        order = models.Order.objects.get(id=order_id)
    except models.Order.DoesNotExist:
        raise Http404
    if request.method == "GET":
        orderItemSerializer = serializers.OrderItemSerializer(order.orderitem_set,many=True)
        return Response(orderItemSerializer.data)
    if request.method == "POST":
        orderItemSerializer = serializers.OrderItemSerializer(data=request.data)
        if not orderItemSerializer.is_valid():
            return HttpResponseBadRequest()
        menuitem = orderItemSerializer.validated_data['item']
        if orderItemSerializer.validated_data['is_set']:
            item_price = menuitem.price+menuitem.set_price
        else:
            item_price = menuitem.price
        item = models.OrderItem.objects.create(
            order = order,
            item = menuitem,
            price = item_price,
            amount= orderItemSerializer.validated_data['amount'],
            is_set= orderItemSerializer.validated_data['is_set'],
            name = menuitem.name
        )
        response_serializer = serializers.OrderItemSerializer(item)
        return Response(response_serializer.data)


@api_view(['PUT', 'DELETE'])
def orderItemDetailView(request, order_id, item_id):
    try:
        order = models.Order.objects.get(id=order_id)
    except models.Order.DoesNotExist:
        raise Http404
    try:
        item = models.Order.objects.get(id=item_id)
    except models.OrderItem.DoesNotExist:
        raise Http404
    if not item.orderitem_set == order:
        return HttpResponseBadRequest()
    if request.method == "PUT":
        itemSerializer = serializers.OrderItemSerializer(data=request.data)
        if not itemSerializer.is_valid():
            return HttpResponseBadRequest()
        itemSerializer.update(instance=item, validated_data=itemSerializer.validated_data)
        return Response(data=itemSerializer.data)
    if request.method == "DELETE":
        item.delete()
        return Response(status=200)
