from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=["id","first_name","second_name","email"]

class WaiterAdmin(admin.ModelAdmin):
    list_display=["id","user","charge"]

admin.site.register(User,UserAdmin)
admin.site.register(Waiter, WaiterAdmin)