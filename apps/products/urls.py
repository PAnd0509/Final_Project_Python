from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'product',ProductViewSet,basename='product')
urlpatterns=[
    
]

urlpatterns+=router.urls