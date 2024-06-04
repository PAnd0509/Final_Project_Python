from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Waiter
        fields="__all__"