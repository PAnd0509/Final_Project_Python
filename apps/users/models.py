from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name=models.CharField(max_length=10, null=False, blank=False)
    second_name=models.CharField(max_length=10, null=False, blank=False)
    email=models.EmailField(null=False, blank=False)

class Waiter(models.Model):
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ROL={
        ("MG","MANAGER"),
        ("AT","ADMINTABLES"),
        ("EX","EXTRA")
    }
    charge=models.CharField(max_length=2, choices=ROL,default="EX")

    

