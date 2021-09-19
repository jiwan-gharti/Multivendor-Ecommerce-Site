from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumber

# Create your models here.
SHIPPING_ADDRESS = (
    ('Office', 'Office'),
    ('Home', 'Home'),
)

class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=100)
    receiver_no = PhoneNumber(country_code="+977")
    region = models.CharField(max_length=100)
    city   = models.CharField(max_length=100)
    area   = models.CharField(max_length=100)
    address = models.CharField(max_length=100, help_text="House# 001")
    label   = models.CharField(max_length=8, choices=SHIPPING_ADDRESS)

    def __str__(self):
        return f'{self.full_name}-{self.area}'

class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    mobile = PhoneNumber(country_code="+977")

    def __str__(self):
        return self.user