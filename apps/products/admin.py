from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=["name","cost_per_unit","all_restaurants"]

admin.site.register(Product,ProductAdmin)