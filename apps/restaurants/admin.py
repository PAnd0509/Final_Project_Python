from django.contrib import admin
from .models import *
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display=["number","PersonCapacity"]

class RestaurantAdmin(admin.ModelAdmin):
    list_display=["name","direcction","user"]

class Products_restaurantAdmin(admin.ModelAdmin):
    list_display=["product","restaurant"]

class Tables_restaurantAdmin(admin.ModelAdmin):
    list_display=["table","restaurant"]

class OrderAdmin(admin.ModelAdmin):
    list_display=["waiter","table_restaurant"]

class BillAdmin(admin.ModelAdmin):
    list_display=["order","cost","tip_porcent","final_cost"]

class Products_orderAdmin(admin.ModelAdmin):
    list_display=["product","order"]

class Tip_waiterAdmin(admin.ModelAdmin):
    list_display=["bill","waiter","paid"]

class Waiter_shiftAdmin(admin.ModelAdmin):
    list_display=["waiter","start_date","end_date","restaurant"]
    
admin.site.register(Table,TableAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Products_restaurant,Products_restaurantAdmin)
admin.site.register(Tables_restaurant,Tables_restaurantAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Bill,BillAdmin)
admin.site.register(Products_order,Products_orderAdmin)
admin.site.register(Tip_waiter,Tip_waiterAdmin)
admin.site.register(Waiter_shift,Waiter_shiftAdmin)