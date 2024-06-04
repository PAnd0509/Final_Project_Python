from django.shortcuts import render
from .models import *
from .serializers import *
from apps.users.permitions import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class TableViewSet(ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=TableSerializer

    @action(detail=False, methods=['get'])
    def for_waiter(self, request):
        aux_waiter_id = request.query_params.get('waiter_id')
        if aux_waiter_id:
            current_shifts = Waiter_shift.objects.filter(
                waiter_id=aux_waiter_id,
                start_date__lte=timezone.now(),
                end_date__gte=timezone.now()
            )
            tables = Table.objects.filter(tables_restaurant__restaurant__waiter_shift__in=current_shifts)
        else:
            tables = Table.objects.none()
        serializer = self.get_serializer(tables, many=True)
        return Response(serializer.data)
    
class RestaurantViewSet(ModelViewSet):
    queryset=Restaurant.objects.all()
    serializer_class=RestaurantSerializer

class Products_restaurantViewSet(ModelViewSet):
    serializer_class=Products_restaurantSerializer
    def get_queryset(self):
        queryset = Products_restaurant.objects.all()
        restaurant_id = self.request.query_params.get('restaurant_id', None)
        if restaurant_id is not None:
            queryset = queryset.filter(restaurant__id=restaurant_id)
        return queryset

class Tables_restaurantViewSet(ModelViewSet):
    queryset=Tables_restaurant.objects.all()
    serializer_class=Tables_restaurantSerializer
    

class OrderViewSet(ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    def get_permissions(self):
        if self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated,IsManage, IsAdminTables]
        return super().get_permissions()

class BillViewSet(ModelViewSet):
    queryset=Bill.objects.all()
    serializer_class=BillSerializer
    
    def get_permissions(self):
        if self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated,IsManage]
        return super().get_permissions()

class Products_orderViewSet(ModelViewSet):
    queryset=Products_order.objects.all()
    serializer_class=Products_orderSerializer


class Tip_waiterViewSet(ModelViewSet):
    queryset=Tip_waiter.objects.all()
    serializer_class=Tip_waiterSerializer

class Waiter_shiftViewSet(ModelViewSet):
    queryset=Waiter_shift.objects.all()
    serializer_class=Waiter_shiftSerializer