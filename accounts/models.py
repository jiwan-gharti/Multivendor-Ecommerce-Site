from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(User):
    username = None
    gender = [
        ("Male", 'Male'),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    phone_number = PhoneNumberField(region="NP")
    address      = models.CharField(max_length=200)
    gender       = models.CharField(max_length=6, choices=gender)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


