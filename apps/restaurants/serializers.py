from rest_framework import serializers
from .models import *

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"

class RestaurantSerializer(serializers. ModelSerializer):
    class Meta:
        model=Restaurant
        fields="__all__"

class Products_restaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products_restaurant
        fields="__all__"

class Tables_restaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tables_restaurant
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields="__all__"

class Products_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products_order
        fields="__all__"

class Tip_waiterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tip_waiter
        fields="__all__"

class Waiter_shiftSerializer(serializers.ModelSerializer):
    class Meta:
        model=Waiter_shift
        fields="__all__"
    