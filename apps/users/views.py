from django.shortcuts import render
from .serializers import *
from apps.restaurants.serializers import OrderSerializer, Waiter_shift, Order
# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class WaiterViewSet(ModelViewSet):
    
    queryset=Waiter.objects.all()
    serializer_class=WaiterSerializer
    @action(detail=True, methods=['post'], url_path='add_shift')
    def add_shift(self, request, pk=None):
        waiter = self.get_object()
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        restaurant_id = request.data.get('restaurant')

        shift = Waiter_shift.objects.create(
            waiter=waiter,
            start_date=start_date,
            end_date=end_date,
            restaurant_id=restaurant_id
        )
        return Response({'status': 'shift added'}, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'], url_path='orders')
    def my_order(self, request, pk=None):
        waiter = Waiter.objects.get(pk=pk)
        active = request.query_params.get('active')

        if active:
            orders = Order.objects.filter(waiter=waiter, bill__final_cost__isnull=True)
        else:
            orders = Order.objects.filter(waiter=waiter)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    