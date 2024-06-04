from django.db import models
from apps.users.models import *
from apps.products.models import Product
# Create your models here.
class Table(models.Model):
    number = models.PositiveIntegerField(null=False, blank=False)
    PersonCapacity = models.PositiveIntegerField(null=False, blank=False)

class Restaurant(models.Model):
    name=models.CharField(max_length=60, null=False, blank=False)
    direcction= models.CharField(max_length=60, null=False, blank=False)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Products_restaurant(models.Model):
    product=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)

class Tables_restaurant(models.Model):
    table=models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)

class Order(models.Model):
    waiter=models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    table_restaurant=models.ForeignKey(Tables_restaurant, on_delete=models.DO_NOTHING)

class Bill(models.Model):
    order=models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    cost=models.PositiveIntegerField(null=False, blank=False)
    tip_porcent=models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    final_cost=models.DecimalField(max_digits=10,decimal_places=2, null=False, blank=False)

class Products_order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order=models.ForeignKey(Order, on_delete=models.DO_NOTHING)

class Tip_waiter(models.Model):
    bill=models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    waiter=models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    paid=models.BooleanField(default=True)

class Waiter_shift(models.Model):
    waiter=models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    restaurant=models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    