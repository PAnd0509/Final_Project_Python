from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'table',TableViewSet,basename='table')
router.register(r'restaurant', RestaurantViewSet,basename='restaurant')
router.register(r'product_restaurant', Products_restaurantViewSet,basename='product_restaurant')
router.register(r'table_restaurant', Tables_restaurantViewSet,basename='table_restaurant')
router.register(r'order', OrderViewSet,basename='order')
router.register(r'bill', BillViewSet,basename='bill')
router.register(r'product_order', Products_orderViewSet,basename='product_order')
router.register(r'tip_waiter', Tip_waiterViewSet,basename='tip_waiter')
router.register(r'waiter_shift', Waiter_shiftViewSet,basename='waiter_shift')

urlpatterns=[
    
]
urlpatterns+=router.urls
