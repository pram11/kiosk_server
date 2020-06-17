from django.db import models
from menu.models import MenuItem
# Create your models here.


ORDER_STATUS = (('ordering','ordering'),('ordered','ordered'),('delivered','delivered'),('canceled','canceled'))


class Order(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    waiting_num = models.PositiveIntegerField(null=True,blank=True)
    status = models.CharField(choices=ORDER_STATUS,max_length=10)
    #주문 처리 기능 추가할 경우 생성
    #user = models.ForeignKey(User,on_delete = models.DO_NOTHING)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem,on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField()
    is_set = models.BooleanField(default=False)
    amount = models.PositiveIntegerField()
