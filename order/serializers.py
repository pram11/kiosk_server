from rest_framework import serializers
from order import models

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=models.ORDER_STATUS)
    create_date = serializers.DateTimeField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)
    waiting_num = serializers.IntegerField(required=False)
    class Meta:
        model = models.Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    set_price = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.OrderItem
        fields = ['order','item','price','is_set','amount','name','set_price']
