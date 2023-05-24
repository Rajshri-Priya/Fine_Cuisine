from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# class User(AbstractUser):
#     mobile_num = models.IntegerField()
#     location = models.CharField(max_length=100)
class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        # ('manager', 'Manager'),
        # ('waiter', 'Waiter'),

    )

    role = models.CharField(max_length=10, choices=ROLES)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)


# class Staff(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     position = models.CharField(max_length=50)
#     department = models.CharField(max_length=50)
#     shift = models.CharField(max_length=50)