from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_use = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=300)
    cateogy = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_use = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name

class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()
    is_use = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.item.name

class Transaction(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)