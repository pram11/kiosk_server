from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=20)


class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE,related_name='items')
    image = models.ImageField(null=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    set_price = models.IntegerField()
    set_available = models.BooleanField(default=True)

