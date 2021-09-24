from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    gender = [
        ("Male", 'Male'),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    phone_number = PhoneNumberField(region="NP")
    address      = models.CharField(max_length=200,null=True, blank=True)
    gender       = models.CharField(max_length=6, choices=gender)
    is_customer  = models.BooleanField(default=False)
    is_merchant  = models.BooleanField(default=False)
    pan_no       =     models.BigIntegerField("User Pan Number", unique=True, null=True, blank=True)
    document     = models.ImageField(upload_to="merchant documents", null=True, blank = True)


    def __str__(self):
        return self.username




    # def __str__(self):
    #     return str(self.pan_no)


